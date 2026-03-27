import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Sidebar Logo with SVG Seal
sidebar_header_old = r'<!-- Sidebar Header with Logo -->.*?<h3 class="text-heritage-cream font-black text-lg">ديوان قبيلة الحياني</h3>'
sidebar_header_new = """<!-- Sidebar Header with Logo -->
            <div class="mb-10 relative flex flex-col items-center">
                <div class="absolute inset-0 bg-heritage-gold blur-3xl opacity-20"></div>
                <div class="relative w-28 h-28 flex items-center justify-center mb-4">
                    <svg viewBox="0 0 200 200" class="w-full h-full drop-shadow-[0_0_15px_rgba(212,175,55,0.4)]">
                        <circle cx="100" cy="100" r="95" fill="none" stroke="#d4af37" stroke-width="1" stroke-dasharray="5 5" class="animate-[spin_30s_linear_infinite]" />
                        <circle cx="100" cy="100" r="80" fill="rgba(0,0,0,0.6)" stroke="#d4af37" stroke-width="3" />
                        <text x="50%" y="115" text-anchor="middle" font-family="Cairo" font-weight="900" font-size="36" fill="#d4af37">H</text>
                    </svg>
                </div>
                <h3 class="text-heritage-gold font-black text-xl tracking-wide">ديوان السيادة</h3>"""

content = re.sub(sidebar_header_old, sidebar_header_new, content, flags=re.DOTALL)

# 2. Make Control Panel Button in Sidebar more prominent
control_btn_old = r'<!-- 8. لوحة التحكم -->.*?<span class="text-lg">⚙️</span>\s*</button>'
control_btn_new = """<!-- 8. لوحة التحكم -->
            <button onclick="toggleAdmin();" class="w-full py-4 px-4 bg-heritage-neonBlue/20 text-heritage-neonBlue rounded-2xl border-2 border-heritage-neonBlue/40 font-black text-right flex items-center justify-between hover:bg-heritage-neonBlue hover:text-black transition-all shadow-[0_0_20px_rgba(0,242,255,0.1)] hover:shadow-[0_0_30px_rgba(0,242,255,0.3)]">
                <span class="text-sm">٨. لوحة التحكم (السيادة)</span>
                <span class="text-2xl animate-spin-slow">⚙️</span>
            </button>"""

content = re.sub(control_btn_old, control_btn_new, content, flags=re.DOTALL)

# Add spin-slow animation if missing
if '.animate-spin-slow' not in content:
    content = content.replace('</style>', '        .animate-spin-slow { animation: spin 8s linear infinite; }\n        @keyframes spin { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }\n    </style>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
