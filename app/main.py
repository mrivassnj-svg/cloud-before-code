from fastapi import FastAPI, Request, Form, Depends, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from itsdangerous import URLSafeTimedSerializer, BadSignature
from sqlalchemy.orm import Session
from pathlib import Path
import os

from database import init_db, get_db, Lesson, Term
from ai import probe_and_rank, explain_it_back, check_exit_question

# ── Per-lesson SVG illustrations (shown before exit questions) ────────────────
# Each is a compact inline SVG (≤ 320×160) depicting the lesson's everyday analogy.

LESSON_SVGS = {
    1: """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 160" role="img" aria-label="A person at an ATM asking a bank mainframe for their balance">
  <!-- sky background -->
  <rect width="320" height="160" fill="#f0f4ff"/>
  <!-- ATM machine -->
  <rect x="20" y="40" width="60" height="90" rx="6" fill="#3b82d4" stroke="#2563b0" stroke-width="1.5"/>
  <rect x="30" y="52" width="40" height="28" rx="3" fill="#bfdbfe"/>
  <text x="50" y="70" font-size="8" fill="#1e3a5f" text-anchor="middle" font-family="sans-serif">ATM</text>
  <rect x="33" y="88" width="34" height="10" rx="2" fill="#93c5fd"/>
  <rect x="33" y="102" width="34" height="6" rx="1" fill="#60a5fa"/>
  <!-- person -->
  <circle cx="110" cy="62" r="12" fill="#fde68a" stroke="#d97706" stroke-width="1.5"/>
  <line x1="110" y1="74" x2="110" y2="108" stroke="#374151" stroke-width="2.5"/>
  <line x1="110" y1="82" x2="90" y2="94" stroke="#374151" stroke-width="2"/>
  <line x1="110" y1="82" x2="130" y2="94" stroke="#374151" stroke-width="2"/>
  <line x1="110" y1="108" x2="96" y2="128" stroke="#374151" stroke-width="2"/>
  <line x1="110" y1="108" x2="124" y2="128" stroke="#374151" stroke-width="2"/>
  <!-- arrow right: request -->
  <line x1="135" y1="80" x2="195" y2="80" stroke="#3b82d4" stroke-width="2" stroke-dasharray="4,3"/>
  <polygon points="195,76 203,80 195,84" fill="#3b82d4"/>
  <text x="166" y="74" font-size="8" fill="#3b82d4" text-anchor="middle" font-family="sans-serif">request</text>
  <!-- arrow left: response -->
  <line x1="195" y1="96" x2="135" y2="96" stroke="#059669" stroke-width="2" stroke-dasharray="4,3"/>
  <polygon points="135,92 127,96 135,100" fill="#059669"/>
  <text x="166" y="110" font-size="8" fill="#059669" text-anchor="middle" font-family="sans-serif">response</text>
  <!-- server rack -->
  <rect x="206" y="38" width="80" height="90" rx="5" fill="#1e3a5f"/>
  <rect x="214" y="48" width="64" height="10" rx="2" fill="#3b82d4"/>
  <rect x="214" y="62" width="64" height="10" rx="2" fill="#3b82d4"/>
  <rect x="214" y="76" width="64" height="10" rx="2" fill="#3b82d4"/>
  <circle cx="270" cy="53" r="3" fill="#34d399"/>
  <circle cx="270" cy="67" r="3" fill="#34d399"/>
  <circle cx="270" cy="81" r="3" fill="#fbbf24"/>
  <text x="246" y="108" font-size="8" fill="#93c5fd" text-anchor="middle" font-family="sans-serif">Cloud Server</text>
  <!-- labels -->
  <text x="50" y="140" font-size="9" fill="#374151" text-anchor="middle" font-family="sans-serif">Client device</text>
  <text x="246" y="140" font-size="9" fill="#374151" text-anchor="middle" font-family="sans-serif">Server (data lives here)</text>
</svg>""",

    2: """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 160" role="img" aria-label="Library shelves on the left and a card catalog on the right">
  <rect width="320" height="160" fill="#fdf8f0"/>
  <!-- Left: shelves (object storage) -->
  <rect x="10" y="20" width="130" height="130" rx="4" fill="#fef3c7" stroke="#d97706" stroke-width="1.2"/>
  <text x="75" y="36" font-size="9" font-weight="bold" fill="#92400e" text-anchor="middle" font-family="sans-serif">Object Storage</text>
  <!-- shelf lines -->
  <line x1="20" y1="55" x2="130" y2="55" stroke="#d97706" stroke-width="1.5"/>
  <line x1="20" y1="90" x2="130" y2="90" stroke="#d97706" stroke-width="1.5"/>
  <line x1="20" y1="125" x2="130" y2="125" stroke="#d97706" stroke-width="1.5"/>
  <!-- books on shelf 1 -->
  <rect x="22" y="40" width="12" height="14" rx="1" fill="#f59e0b"/>
  <rect x="36" y="40" width="12" height="14" rx="1" fill="#3b82d4"/>
  <rect x="50" y="40" width="12" height="14" rx="1" fill="#059669"/>
  <rect x="64" y="40" width="12" height="14" rx="1" fill="#dc2626"/>
  <!-- photo icons on shelf 2 -->
  <rect x="22" y="66" width="18" height="14" rx="2" fill="#93c5fd"/>
  <text x="31" y="76" font-size="8" fill="#1e3a5f" text-anchor="middle" font-family="sans-serif">JPG</text>
  <rect x="44" y="66" width="18" height="14" rx="2" fill="#93c5fd"/>
  <text x="53" y="76" font-size="8" fill="#1e3a5f" text-anchor="middle" font-family="sans-serif">MP4</text>
  <rect x="66" y="66" width="18" height="14" rx="2" fill="#93c5fd"/>
  <text x="75" y="76" font-size="8" fill="#1e3a5f" text-anchor="middle" font-family="sans-serif">PDF</text>
  <text x="75" y="145" font-size="8" fill="#92400e" text-anchor="middle" font-family="sans-serif">whole files, retrieved as-is</text>

  <!-- Right: card catalog (database) -->
  <rect x="180" y="20" width="130" height="130" rx="4" fill="#dcfce7" stroke="#059669" stroke-width="1.2"/>
  <text x="245" y="36" font-size="9" font-weight="bold" fill="#166534" text-anchor="middle" font-family="sans-serif">Database</text>
  <!-- rows -->
  <rect x="192" y="44" width="106" height="12" rx="2" fill="#bbf7d0"/>
  <text x="245" y="53" font-size="7" fill="#166534" text-anchor="middle" font-family="sans-serif">Order #1042 · Jordan · 12:03pm</text>
  <rect x="192" y="60" width="106" height="12" rx="2" fill="#bbf7d0"/>
  <text x="245" y="69" font-size="7" fill="#166534" text-anchor="middle" font-family="sans-serif">Order #1043 · Sam · 12:04pm</text>
  <rect x="192" y="76" width="106" height="12" rx="2" fill="#bbf7d0"/>
  <text x="245" y="85" font-size="7" fill="#166534" text-anchor="middle" font-family="sans-serif">Order #1044 · Riley · 12:05pm</text>
  <!-- search magnifier -->
  <circle cx="232" cy="112" r="12" fill="none" stroke="#059669" stroke-width="2"/>
  <line x1="241" y1="121" x2="252" y2="132" stroke="#059669" stroke-width="2.5" stroke-linecap="round"/>
  <text x="232" y="115" font-size="10" fill="#059669" text-anchor="middle" font-family="sans-serif">?</text>
  <text x="245" y="150" font-size="8" fill="#166534" text-anchor="middle" font-family="sans-serif">searchable, filterable records</text>
</svg>""",

    3: """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 160" role="img" aria-label="Three workspace options: empty office, managed office, co-working hot desk">
  <rect width="320" height="160" fill="#f8fafc"/>
  <!-- Option A: VM = empty office -->
  <rect x="8" y="20" width="88" height="100" rx="5" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
  <text x="52" y="36" font-size="8" font-weight="bold" fill="#92400e" text-anchor="middle" font-family="sans-serif">Virtual Machine</text>
  <!-- desk + chair simple -->
  <rect x="20" y="82" width="64" height="8" rx="2" fill="#d97706"/>
  <rect x="38" y="90" width="8" height="18" rx="1" fill="#b45309"/>
  <rect x="20" y="60" width="20" height="20" rx="2" fill="#93c5fd"/>
  <text x="30" y="73" font-size="7" fill="#1e3a5f" text-anchor="middle" font-family="sans-serif">OS</text>
  <text x="52" y="118" font-size="7" fill="#92400e" text-anchor="middle" font-family="sans-serif">full control</text>
  <text x="52" y="128" font-size="7" fill="#92400e" text-anchor="middle" font-family="sans-serif">you manage all</text>

  <!-- Option B: Container = managed office -->
  <rect x="116" y="20" width="88" height="100" rx="5" fill="#dbeafe" stroke="#3b82d4" stroke-width="1.5"/>
  <text x="160" y="36" font-size="8" font-weight="bold" fill="#1e3a5f" text-anchor="middle" font-family="sans-serif">Container</text>
  <!-- furnished desk -->
  <rect x="128" y="82" width="64" height="8" rx="2" fill="#3b82d4"/>
  <rect x="146" y="90" width="8" height="18" rx="1" fill="#2563b0"/>
  <rect x="128" y="62" width="20" height="18" rx="2" fill="#93c5fd"/>
  <text x="138" y="74" font-size="7" fill="#1e3a5f" text-anchor="middle" font-family="sans-serif">App</text>
  <!-- shared utilities indicator -->
  <text x="162" y="56" font-size="7" fill="#2563b0" text-anchor="middle" font-family="sans-serif">shared OS</text>
  <text x="160" y="118" font-size="7" fill="#1e3a5f" text-anchor="middle" font-family="sans-serif">isolated space</text>
  <text x="160" y="128" font-size="7" fill="#1e3a5f" text-anchor="middle" font-family="sans-serif">shared building</text>

  <!-- Option C: Serverless = hot desk -->
  <rect x="224" y="20" width="88" height="100" rx="5" fill="#dcfce7" stroke="#059669" stroke-width="1.5"/>
  <text x="268" y="36" font-size="8" font-weight="bold" fill="#166534" text-anchor="middle" font-family="sans-serif">Serverless</text>
  <!-- hot desk - minimal -->
  <rect x="236" y="82" width="64" height="8" rx="2" fill="#059669" stroke-dasharray="3,2"/>
  <text x="268" y="64" font-size="20" fill="#059669" text-anchor="middle" font-family="sans-serif">⚡</text>
  <text x="268" y="118" font-size="7" fill="#166534" text-anchor="middle" font-family="sans-serif">pay per use</text>
  <text x="268" y="128" font-size="7" fill="#166534" text-anchor="middle" font-family="sans-serif">no setup needed</text>

  <!-- bottom label -->
  <text x="160" y="152" font-size="8" fill="#374151" text-anchor="middle" font-family="sans-serif">More control ◄─────────────────► Less to manage</text>
</svg>""",

    4: """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 160" role="img" aria-label="A package journey from sender through sorting hubs to destination, like DNS and HTTP">
  <rect width="320" height="160" fill="#f0fdf4"/>
  <!-- Sender (phone/browser) -->
  <rect x="8" y="55" width="44" height="56" rx="4" fill="#3b82d4" stroke="#2563b0" stroke-width="1.2"/>
  <rect x="14" y="62" width="32" height="22" rx="2" fill="#bfdbfe"/>
  <text x="30" y="96" font-size="7" fill="#bfdbfe" text-anchor="middle" font-family="sans-serif">Browser</text>
  <text x="30" y="122" font-size="7" fill="#374151" text-anchor="middle" font-family="sans-serif">Client</text>

  <!-- Arrow 1 -->
  <line x1="54" y1="83" x2="80" y2="83" stroke="#6b7280" stroke-width="1.5" stroke-dasharray="3,2"/>
  <polygon points="80,80 86,83 80,86" fill="#6b7280"/>

  <!-- DNS box -->
  <rect x="88" y="62" width="52" height="38" rx="4" fill="#fef9c3" stroke="#d97706" stroke-width="1.2"/>
  <text x="114" y="78" font-size="7" font-weight="bold" fill="#92400e" text-anchor="middle" font-family="sans-serif">DNS</text>
  <text x="114" y="89" font-size="6.5" fill="#92400e" text-anchor="middle" font-family="sans-serif">name → IP</text>
  <text x="114" y="112" font-size="7" fill="#374151" text-anchor="middle" font-family="sans-serif">directory</text>

  <!-- Arrow 2 -->
  <line x1="142" y1="83" x2="168" y2="83" stroke="#6b7280" stroke-width="1.5" stroke-dasharray="3,2"/>
  <polygon points="168,80 174,83 168,86" fill="#6b7280"/>

  <!-- HTTP envelope -->
  <rect x="176" y="60" width="52" height="42" rx="4" fill="#ede9fe" stroke="#7c3aed" stroke-width="1.2"/>
  <text x="202" y="76" font-size="7" font-weight="bold" fill="#5b21b6" text-anchor="middle" font-family="sans-serif">HTTP</text>
  <!-- envelope icon -->
  <rect x="186" y="80" width="32" height="16" rx="1" fill="#c4b5fd"/>
  <polyline points="186,80 202,91 218,80" fill="none" stroke="#5b21b6" stroke-width="1"/>
  <text x="202" y="114" font-size="7" fill="#374151" text-anchor="middle" font-family="sans-serif">standard format</text>

  <!-- Arrow 3 -->
  <line x1="230" y1="83" x2="256" y2="83" stroke="#6b7280" stroke-width="1.5" stroke-dasharray="3,2"/>
  <polygon points="256,80 262,83 256,86" fill="#6b7280"/>

  <!-- Server / API -->
  <rect x="264" y="50" width="50" height="66" rx="4" fill="#1e3a5f" stroke="#1e40af" stroke-width="1.2"/>
  <rect x="272" y="58" width="34" height="8" rx="2" fill="#3b82d4"/>
  <rect x="272" y="70" width="34" height="8" rx="2" fill="#3b82d4"/>
  <text x="289" y="88" font-size="6.5" fill="#93c5fd" text-anchor="middle" font-family="sans-serif">API</text>
  <circle cx="300" cy="62" r="2.5" fill="#34d399"/>
  <circle cx="300" cy="74" r="2.5" fill="#34d399"/>
  <text x="289" y="128" font-size="7" fill="#374151" text-anchor="middle" font-family="sans-serif">Server</text>

  <!-- top label -->
  <text x="160" y="20" font-size="9" fill="#374151" text-anchor="middle" font-family="sans-serif" font-weight="bold">How an order travels: name → address → format → destination</text>
  <text x="160" y="148" font-size="7.5" fill="#6b7280" text-anchor="middle" font-family="sans-serif">(simplified — real paths involve many more hops)</text>
</svg>""",

    5: """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 160" role="img" aria-label="Airport security checkpoint: one lane overwhelmed vs three lanes with a traffic director">
  <rect width="320" height="160" fill="#f8fafc"/>
  <!-- Left panel: 1 lane, overwhelmed -->
  <rect x="5" y="8" width="140" height="144" rx="5" fill="#fee2e2" stroke="#dc2626" stroke-width="1.2"/>
  <text x="75" y="24" font-size="8" font-weight="bold" fill="#991b1b" text-anchor="middle" font-family="sans-serif">1 instance — overwhelmed</text>
  <!-- one lane -->
  <rect x="52" y="34" width="46" height="62" rx="3" fill="#fca5a5" stroke="#dc2626" stroke-width="1"/>
  <text x="75" y="54" font-size="7" fill="#7f1d1d" text-anchor="middle" font-family="sans-serif">App</text>
  <!-- queue of people -->
  <circle cx="30" cy="68" r="5" fill="#fde68a" stroke="#d97706" stroke-width="1"/>
  <circle cx="20" cy="82" r="5" fill="#fde68a" stroke="#d97706" stroke-width="1"/>
  <circle cx="30" cy="96" r="5" fill="#fde68a" stroke="#d97706" stroke-width="1"/>
  <circle cx="20" cy="110" r="5" fill="#fde68a" stroke="#d97706" stroke-width="1"/>
  <circle cx="30" cy="124" r="5" fill="#fde68a" stroke="#d97706" stroke-width="1"/>
  <!-- clock showing slow -->
  <text x="75" y="130" font-size="22" text-anchor="middle" font-family="sans-serif">🐢</text>
  <text x="75" y="148" font-size="8" fill="#991b1b" text-anchor="middle" font-family="sans-serif">18 s per order</text>

  <!-- Right panel: 3 lanes + load balancer -->
  <rect x="175" y="8" width="140" height="144" rx="5" fill="#dcfce7" stroke="#059669" stroke-width="1.2"/>
  <text x="245" y="24" font-size="8" font-weight="bold" fill="#166534" text-anchor="middle" font-family="sans-serif">3 instances + load balancer</text>
  <!-- load balancer funnel -->
  <polygon points="245,30 225,46 265,46" fill="#059669"/>
  <!-- three lanes -->
  <rect x="192" y="52" width="30" height="44" rx="2" fill="#bbf7d0" stroke="#059669" stroke-width="1"/>
  <text x="207" y="77" font-size="7" fill="#166534" text-anchor="middle" font-family="sans-serif">App</text>
  <rect x="230" y="52" width="30" height="44" rx="2" fill="#bbf7d0" stroke="#059669" stroke-width="1"/>
  <text x="245" y="77" font-size="7" fill="#166534" text-anchor="middle" font-family="sans-serif">App</text>
  <rect x="268" y="52" width="30" height="44" rx="2" fill="#bbf7d0" stroke="#059669" stroke-width="1"/>
  <text x="283" y="77" font-size="7" fill="#166534" text-anchor="middle" font-family="sans-serif">App</text>
  <!-- arrows from balancer -->
  <line x1="237" y1="46" x2="207" y2="52" stroke="#059669" stroke-width="1.2"/>
  <line x1="245" y1="46" x2="245" y2="52" stroke="#059669" stroke-width="1.2"/>
  <line x1="253" y1="46" x2="283" y2="52" stroke="#059669" stroke-width="1.2"/>
  <text x="245" y="130" font-size="22" text-anchor="middle" font-family="sans-serif">⚡</text>
  <text x="245" y="148" font-size="8" fill="#166534" text-anchor="middle" font-family="sans-serif">2 s per order</text>
</svg>""",

    6: """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 160" role="img" aria-label="Four staff members with ID badges and different door-access permissions">
  <rect width="320" height="160" fill="#f0f4ff"/>
  <!-- Building outline -->
  <rect x="10" y="30" width="300" height="110" rx="6" fill="#fff" stroke="#c7d7f8" stroke-width="1.5"/>
  <text x="160" y="22" font-size="9" font-weight="bold" fill="#374151" text-anchor="middle" font-family="sans-serif">LunchRush Access Control</text>

  <!-- Jordan — full access (green badge) -->
  <circle cx="45" cy="80" r="14" fill="#fde68a" stroke="#d97706" stroke-width="1.5"/>
  <text x="45" y="84" font-size="8" fill="#374151" text-anchor="middle" font-family="sans-serif">Jordan</text>
  <rect x="31" y="98" width="28" height="12" rx="3" fill="#059669"/>
  <text x="45" y="107" font-size="6.5" fill="#fff" text-anchor="middle" font-family="sans-serif">ALL ACCESS</text>
  <text x="45" y="124" font-size="7" fill="#374151" text-anchor="middle" font-family="sans-serif">Owner</text>

  <!-- Sam — menu only (yellow badge) -->
  <circle cx="115" cy="80" r="14" fill="#fde68a" stroke="#d97706" stroke-width="1.5"/>
  <text x="115" y="84" font-size="8" fill="#374151" text-anchor="middle" font-family="sans-serif">Sam</text>
  <rect x="101" y="98" width="28" height="12" rx="3" fill="#f59e0b"/>
  <text x="115" y="107" font-size="6.5" fill="#fff" text-anchor="middle" font-family="sans-serif">MENU ONLY</text>
  <text x="115" y="124" font-size="7" fill="#374151" text-anchor="middle" font-family="sans-serif">Content</text>

  <!-- Riley — orders only (blue badge) -->
  <circle cx="185" cy="80" r="14" fill="#fde68a" stroke="#d97706" stroke-width="1.5"/>
  <text x="185" y="84" font-size="8" fill="#374151" text-anchor="middle" font-family="sans-serif">Riley</text>
  <rect x="171" y="98" width="28" height="12" rx="3" fill="#3b82d4"/>
  <text x="185" y="107" font-size="6.5" fill="#fff" text-anchor="middle" font-family="sans-serif">ORDERS</text>
  <text x="185" y="124" font-size="7" fill="#374151" text-anchor="middle" font-family="sans-serif">Delivery</text>

  <!-- Alex — tech config (purple badge) -->
  <circle cx="255" cy="80" r="14" fill="#fde68a" stroke="#d97706" stroke-width="1.5"/>
  <text x="255" y="84" font-size="8" fill="#374151" text-anchor="middle" font-family="sans-serif">Alex</text>
  <rect x="241" y="98" width="28" height="12" rx="3" fill="#7c3aed"/>
  <text x="255" y="107" font-size="6.5" fill="#fff" text-anchor="middle" font-family="sans-serif">TECH CFG</text>
  <text x="255" y="124" font-size="7" fill="#374151" text-anchor="middle" font-family="sans-serif">Tech</text>

  <!-- lock icon in center at top -->
  <text x="300" y="50" font-size="20" text-anchor="middle" font-family="sans-serif">🔒</text>
  <text x="160" y="148" font-size="7.5" fill="#6b7280" text-anchor="middle" font-family="sans-serif">Authentication proves who you are · Authorization decides what you can do</text>
</svg>""",

    7: """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 160" role="img" aria-label="A CI/CD pipeline as a road construction quality-check sequence with five stations">
  <rect width="320" height="160" fill="#f0fdf4"/>
  <text x="160" y="18" font-size="9" font-weight="bold" fill="#374151" text-anchor="middle" font-family="sans-serif">Release Pipeline — Change to Production</text>

  <!-- pipeline road -->
  <rect x="10" y="80" width="300" height="10" rx="2" fill="#d1d5db"/>

  <!-- Stage boxes -->
  <!-- 1. Code -->
  <rect x="10" y="52" width="46" height="36" rx="4" fill="#bfdbfe" stroke="#3b82d4" stroke-width="1.2"/>
  <text x="33" y="68" font-size="7" font-weight="bold" fill="#1e3a5f" text-anchor="middle" font-family="sans-serif">Code</text>
  <text x="33" y="78" font-size="6.5" fill="#1e3a5f" text-anchor="middle" font-family="sans-serif">change</text>
  <!-- 2. Build -->
  <rect x="68" y="52" width="46" height="36" rx="4" fill="#bfdbfe" stroke="#3b82d4" stroke-width="1.2"/>
  <text x="91" y="68" font-size="7" font-weight="bold" fill="#1e3a5f" text-anchor="middle" font-family="sans-serif">Build</text>
  <text x="91" y="78" font-size="6.5" fill="#1e3a5f" text-anchor="middle" font-family="sans-serif">compile</text>
  <!-- 3. Test (CI) -->
  <rect x="126" y="52" width="46" height="36" rx="4" fill="#fef9c3" stroke="#d97706" stroke-width="1.5"/>
  <text x="149" y="65" font-size="7" font-weight="bold" fill="#92400e" text-anchor="middle" font-family="sans-serif">Test</text>
  <text x="149" y="75" font-size="6.5" fill="#92400e" text-anchor="middle" font-family="sans-serif">CI checks</text>
  <text x="149" y="85" font-size="13" text-anchor="middle" font-family="sans-serif">✓</text>
  <!-- 4. Approve (CD gap) -->
  <rect x="184" y="52" width="46" height="36" rx="4" fill="#ede9fe" stroke="#7c3aed" stroke-width="1.5" stroke-dasharray="4,2"/>
  <text x="207" y="65" font-size="7" font-weight="bold" fill="#5b21b6" text-anchor="middle" font-family="sans-serif">Approve</text>
  <text x="207" y="75" font-size="6.5" fill="#5b21b6" text-anchor="middle" font-family="sans-serif">human gate</text>
  <text x="207" y="85" font-size="10" text-anchor="middle" font-family="sans-serif">👤</text>
  <!-- 5. Deploy -->
  <rect x="242" y="52" width="46" height="36" rx="4" fill="#dcfce7" stroke="#059669" stroke-width="1.2"/>
  <text x="265" y="68" font-size="7" font-weight="bold" fill="#166534" text-anchor="middle" font-family="sans-serif">Deploy</text>
  <text x="265" y="78" font-size="6.5" fill="#166534" text-anchor="middle" font-family="sans-serif">go live</text>

  <!-- arrows between stages -->
  <polygon points="58,76 65,80 58,84" fill="#6b7280"/>
  <polygon points="116,76 123,80 116,84" fill="#6b7280"/>
  <polygon points="174,76 181,80 174,84" fill="#6b7280"/>
  <polygon points="232,76 239,80 232,84" fill="#6b7280"/>

  <!-- CD label (dashed = optional approval) -->
  <text x="207" y="108" font-size="7" fill="#7c3aed" text-anchor="middle" font-family="sans-serif">dashed = delivery only</text>

  <text x="160" y="130" font-size="8" fill="#374151" text-anchor="middle" font-family="sans-serif">Continuous Integration stops here ↑ · Continuous Delivery/Deployment continues →</text>
  <text x="160" y="148" font-size="7.5" fill="#6b7280" text-anchor="middle" font-family="sans-serif">A pipeline reduces risk — it does not guarantee zero bugs.</text>
</svg>""",

    8: """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 160" role="img" aria-label="A doctor's patient chart showing metrics, logs and an alert, next to a question mark for root cause">
  <rect width="320" height="160" fill="#fff7ed"/>
  <!-- Chart clipboard -->
  <rect x="20" y="20" width="160" height="128" rx="5" fill="#fff" stroke="#d97706" stroke-width="1.5"/>
  <rect x="20" y="20" width="160" height="22" rx="5" fill="#fde68a"/>
  <text x="100" y="35" font-size="9" font-weight="bold" fill="#92400e" text-anchor="middle" font-family="sans-serif">Patient Chart — LunchRush App</text>

  <!-- Metric row -->
  <text x="30" y="58" font-size="8" font-weight="bold" fill="#374151" font-family="sans-serif">METRIC</text>
  <text x="30" y="70" font-size="8" fill="#dc2626" font-family="sans-serif">Order time: 12 s  (normal: 2 s) ⚠</text>
  <text x="30" y="82" font-size="8" fill="#dc2626" font-family="sans-serif">CPU: 91%  ⚠</text>

  <!-- Log row -->
  <text x="30" y="98" font-size="8" font-weight="bold" fill="#374151" font-family="sans-serif">LOG</text>
  <text x="30" y="110" font-size="7.5" fill="#374151" font-family="sans-serif">12:03:01 TIMEOUT /api/order</text>
  <text x="30" y="122" font-size="7.5" fill="#374151" font-family="sans-serif">12:03:04 TIMEOUT /api/order</text>
  <text x="30" y="134" font-size="7.5" fill="#374151" font-family="sans-serif">12:03:09 TIMEOUT /api/order</text>

  <!-- Alert badge -->
  <rect x="128" y="52" width="44" height="18" rx="4" fill="#dc2626"/>
  <text x="150" y="64" font-size="8" font-weight="bold" fill="#fff" text-anchor="middle" font-family="sans-serif">ALERT 🔔</text>

  <!-- Right: observation vs conclusion -->
  <rect x="196" y="20" width="114" height="128" rx="5" fill="#f0f4ff" stroke="#c7d7f8" stroke-width="1.2"/>
  <text x="253" y="40" font-size="8" font-weight="bold" fill="#1e3a5f" text-anchor="middle" font-family="sans-serif">Observation</text>
  <text x="253" y="52" font-size="7.5" fill="#374151" text-anchor="middle" font-family="sans-serif">Latency spiked.</text>
  <text x="253" y="62" font-size="7.5" fill="#374151" text-anchor="middle" font-family="sans-serif">CPU is high.</text>
  <text x="253" y="72" font-size="7.5" fill="#374151" text-anchor="middle" font-family="sans-serif">3 timeouts logged.</text>

  <line x1="204" y1="84" x2="302" y2="84" stroke="#c7d7f8" stroke-width="1"/>
  <text x="253" y="98" font-size="8" font-weight="bold" fill="#dc2626" text-anchor="middle" font-family="sans-serif">Root cause?</text>
  <text x="253" y="112" font-size="20" text-anchor="middle" font-family="sans-serif">❓</text>
  <text x="253" y="132" font-size="7" fill="#6b7280" text-anchor="middle" font-family="sans-serif">Need more data</text>
  <text x="253" y="142" font-size="7" fill="#6b7280" text-anchor="middle" font-family="sans-serif">before concluding</text>
</svg>""",
}

# ── App setup ──────────────────────────────────────────────────────────────────

app = FastAPI(title="Cloud Before Code")

BASE_DIR = Path(__file__).resolve().parent
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
templates = Jinja2Templates(directory=BASE_DIR / "templates")

# ── Auth config ────────────────────────────────────────────────────────────────

SECRET_KEY = "lunchrush-secret-2026"          # change before any real deployment
SHARED_PASSWORD = "lunchrush123"              # single shared password
serializer = URLSafeTimedSerializer(SECRET_KEY)
COOKIE_NAME = "lunchrush_session"


def make_session_token():
    return serializer.dumps("authenticated")


def verify_session(request: Request):
    token = request.cookies.get(COOKIE_NAME)
    if not token:
        return False
    try:
        value = serializer.loads(token, max_age=86400)  # 24 hours
        return value == "authenticated"
    except BadSignature:
        return False


def require_auth(request: Request):
    if not verify_session(request):
        raise HTTPException(status_code=302, headers={"Location": "/login"})


# ── Startup ────────────────────────────────────────────────────────────────────

@app.on_event("startup")
def startup():
    init_db()


# ── Routes ─────────────────────────────────────────────────────────────────────

@app.get("/login", response_class=HTMLResponse)
async def login_page(request: Request, error: str = ""):
    return templates.TemplateResponse("login.html", {"request": request, "error": error})


@app.post("/login")
async def login(request: Request, password: str = Form(...)):
    if password == SHARED_PASSWORD:
        response = RedirectResponse(url="/", status_code=303)
        response.set_cookie(
            key=COOKIE_NAME,
            value=make_session_token(),
            httponly=True,
            max_age=86400,
            samesite="lax",
        )
        return response
    return templates.TemplateResponse(
        "login.html",
        {"request": request, "error": "Incorrect password. Try again."},
        status_code=401,
    )


@app.get("/logout")
async def logout():
    response = RedirectResponse(url="/login", status_code=303)
    response.delete_cookie(COOKIE_NAME)
    return response


@app.get("/", response_class=HTMLResponse)
async def dashboard(request: Request, db: Session = Depends(get_db)):
    if not verify_session(request):
        return RedirectResponse(url="/login", status_code=303)
    lessons = db.query(Lesson).order_by(Lesson.number).all()
    return templates.TemplateResponse(
        "index.html", {"request": request, "lessons": lessons}
    )


# ── Per-lesson context strings for exit-question AI feedback ─────────────────
LESSON_CONTEXTS = {
    1: "Lesson 1 covers cloud computing (renting computing over the internet), clients (devices that make requests), servers (computers that respond), compute (processing power), and data centers.",
    2: "Lesson 2 covers storage types: object storage (holds whole files like photos/videos, retrieved as-is), buckets (named containers for objects), objects (files plus metadata), and databases (searchable, structured records for orders and customer data).",
    3: "Lesson 3 covers three ways to run an app: virtual machines (full OS control, you manage everything), containers (isolated app package that shares the host OS), and serverless (you provide code, the cloud runs it per execution — servers still exist, you just don't manage them).",
    4: "Lesson 4 covers how data travels: networks (connected devices), IP addresses (numerical device identifiers), DNS (translates domain names to IP addresses), HTTP (standard request/response format for the web), and APIs (contracts defining how software talks to other software).",
    5: "Lesson 5 covers handling load: scaling (adding or upgrading instances to meet demand), application instances (individual running copies of the app), load balancing (distributing traffic across instances), orchestration (automated container management), and Kubernetes (one orchestration tool — not required for all apps).",
    6: "Lesson 6 covers access control: authentication (verifying identity — proving who you are), authorization (determining what an authenticated user can do), IAM (the system of policies managing access), least privilege (grant only what is needed for the job), and shared responsibility (the cloud provider secures the platform; the customer controls access and data).",
    7: "Lesson 7 covers release pipelines: a pipeline (automated build-test-deploy sequence), continuous integration (auto-build and test on every code change), continuous delivery (always deployable, human approves the final release), continuous deployment (fully automated release after tests pass), deployment (putting a new version live), and automation (repeatable steps without manual intervention each time).",
    8: "Lesson 8 covers monitoring: monitoring (continuous collection of system signals), metrics (measured numbers over time like latency and CPU), logs (timestamped event records), alerts (automatic notifications when thresholds are crossed), and latency (time between request and response). Key principle: observations are not the same as root-cause conclusions.",
}


@app.get("/lesson/{number}", response_class=HTMLResponse)
async def lesson_view(number: int, request: Request, db: Session = Depends(get_db)):
    if not verify_session(request):
        return RedirectResponse(url="/login", status_code=303)
    lesson = db.query(Lesson).filter(Lesson.number == number).first()
    if not lesson:
        raise HTTPException(status_code=404, detail="Lesson not found")
    essential = [t for t in lesson.terms if t.essential == 1]
    stretch   = [t for t in lesson.terms if t.essential == 0]
    all_lessons = db.query(Lesson).order_by(Lesson.number).all()
    return templates.TemplateResponse(
        "lesson.html",
        {
            "request": request,
            "lesson": lesson,
            "essential": essential,
            "stretch": stretch,
            "all_lessons": all_lessons,
            "lesson_svg": LESSON_SVGS.get(number, ""),
        },
    )


@app.get("/lesson/{number}/flashcards", response_class=HTMLResponse)
async def flashcards(number: int, request: Request, db: Session = Depends(get_db)):
    if not verify_session(request):
        return RedirectResponse(url="/login", status_code=303)
    lesson = db.query(Lesson).filter(Lesson.number == number).first()
    if not lesson:
        raise HTTPException(status_code=404, detail="Lesson not found")
    terms = [t for t in lesson.terms if t.essential == 1]
    return templates.TemplateResponse(
        "flashcards.html",
        {"request": request, "lesson": lesson, "terms": terms},
    )


# ── AI routes ──────────────────────────────────────────────────────────────────

@app.get("/lesson/{number}/probe", response_class=HTMLResponse)
async def probe_page(number: int, request: Request, db: Session = Depends(get_db)):
    """Show the pre-lesson exploratory question before any vocabulary."""
    if not verify_session(request):
        return RedirectResponse(url="/login", status_code=303)
    lesson = db.query(Lesson).filter(Lesson.number == number).first()
    if not lesson:
        raise HTTPException(status_code=404, detail="Lesson not found")
    return templates.TemplateResponse(
        "probe.html", {"request": request, "lesson": lesson}
    )


@app.post("/lesson/{number}/probe", response_class=HTMLResponse)
async def probe_submit(
    number: int,
    request: Request,
    answer: str = Form(...),
    db: Session = Depends(get_db),
):
    """Process the probe answer through the LLM and show adaptive lesson."""
    if not verify_session(request):
        return RedirectResponse(url="/login", status_code=303)
    lesson = db.query(Lesson).filter(Lesson.number == number).first()
    if not lesson:
        raise HTTPException(status_code=404, detail="Lesson not found")

    result = probe_and_rank(number, answer, db)

    # Build ranked term list
    id_order = {tid: i for i, tid in enumerate(result["ranked_term_ids"])}
    all_terms = db.query(Term).filter(Term.lesson_id == lesson.id).all()
    essential = sorted(
        [t for t in all_terms if t.essential == 1],
        key=lambda t: id_order.get(t.id, 99),
    )
    stretch = [t for t in all_terms if t.essential == 0]
    all_lessons = db.query(Lesson).order_by(Lesson.number).all()

    return templates.TemplateResponse(
        "lesson.html",
        {
            "request": request,
            "lesson": lesson,
            "essential": essential,
            "stretch": stretch,
            "all_lessons": all_lessons,
            "ai_feedback": result["feedback"],
            "understood_words": result["understood_words"],
            "unclear_words": result["unclear_words"],
            "probe_answer": answer,
            "lesson_svg": LESSON_SVGS.get(number, ""),
        },
    )


@app.post("/api/explain-check", response_class=JSONResponse)
async def explain_check(request: Request, db: Session = Depends(get_db)):
    """Check a learner's explanation of a term and return LLM feedback."""
    if not verify_session(request):
        return JSONResponse({"error": "not authenticated"}, status_code=401)
    body = await request.json()
    term_id = body.get("term_id")
    learner_response = body.get("response", "").strip()
    if not term_id or not learner_response:
        return JSONResponse({"error": "missing fields"}, status_code=400)
    term = db.query(Term).filter(Term.id == term_id).first()
    if not term:
        return JSONResponse({"error": "term not found"}, status_code=404)
    result = explain_it_back(term.word, term.definition, learner_response)
    return JSONResponse(result)


@app.post("/api/exit-check", response_class=JSONResponse)
async def exit_check_route(request: Request, db: Session = Depends(get_db)):
    """Evaluate a learner's answer to an exit question with rich AI feedback + hint."""
    if not verify_session(request):
        return JSONResponse({"error": "not authenticated"}, status_code=401)
    body = await request.json()
    lesson_number = body.get("lesson_number")
    question      = body.get("question", "").strip()
    answer        = body.get("answer", "").strip()
    if not lesson_number or not question or not answer:
        return JSONResponse({"error": "missing fields"}, status_code=400)
    context = LESSON_CONTEXTS.get(int(lesson_number), "Cloud computing concepts.")
    result = check_exit_question(question, answer, context)
    return JSONResponse(result)
