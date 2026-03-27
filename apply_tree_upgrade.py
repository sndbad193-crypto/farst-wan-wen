import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add Three.js to head
if 'three.min.js' not in content:
    content = content.replace(
        '<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>',
        '<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>\n    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/0.160.0/three.min.js"></script>'
    )

# 2. Update Sidebar Items
# We need to insert "3D Tree" at #3 and shift others.
sidebar_start = content.find('<div class="w-full space-y-2">')
sidebar_end = content.find('</div>', sidebar_start + 30)
if sidebar_start != -1:
    sidebar_html = """
            <!-- 1. الرئيسية -->
            <button onclick="location.reload();" class="w-full py-3 px-4 bg-white/5 text-white/80 rounded-xl border border-white/10 font-bold text-right flex items-center justify-between hover:bg-heritage-neonBlue hover:text-black transition-all">
                <span class="text-sm">١. الرئيسية</span>
                <span class="text-lg">🏠</span>
            </button>

            <!-- 2. البحث المتقدم -->
            <button onclick="closePanels(); document.getElementById('searchInput').focus();" class="w-full py-3 px-4 bg-white/5 text-white/80 rounded-xl border border-white/10 font-bold text-right flex items-center justify-between hover:bg-heritage-neonBlue hover:text-black transition-all">
                <span class="text-sm">٢. البحث المتقدم</span>
                <span class="text-lg">🔍</span>
            </button>

            <!-- 3. شجرة النسب التفاعلية -->
            <button onclick="openTree();" class="w-full py-3 px-4 bg-white/5 text-white/80 rounded-xl border border-white/10 font-bold text-right flex items-center justify-between hover:bg-heritage-gold hover:text-black transition-all">
                <span class="text-sm">٣. شجرة النسب التفاعلية</span>
                <span class="text-lg">🌳</span>
            </button>

            <!-- 4. الخرائط الجغرافية -->
            <button onclick="openMap();" class="w-full py-3 px-4 bg-white/5 text-white/80 rounded-xl border border-white/10 font-bold text-right flex items-center justify-between hover:bg-heritage-neonBlue hover:text-black transition-all">
                <span class="text-sm">٤. الخرائط الجغرافية</span>
                <span class="text-lg">🗺️</span>
            </button>

            <!-- 5. الإحصائيات والرسوم البيانية -->
            <button onclick="openInfoModal('stats')" class="w-full py-3 px-4 bg-white/5 text-white/80 rounded-xl border border-white/10 font-bold text-right flex items-center justify-between hover:bg-heritage-neonBlue hover:text-black transition-all">
                <span class="text-sm">٥. الإحصائيات والرسوم البيانية</span>
                <span class="text-lg">📊</span>
            </button>

            <!-- 6. المستندات الرسمية -->
            <button onclick="openInfoModal('docs')" class="w-full py-3 px-4 bg-white/5 text-white/80 rounded-xl border border-white/10 font-bold text-right flex items-center justify-between hover:bg-heritage-neonBlue hover:text-black transition-all">
                <span class="text-sm">٦. المستندات الرسمية</span>
                <span class="text-lg">📄</span>
            </button>

            <!-- 7. العقود الذكية (بلوك تشين) -->
            <button onclick="openInfoModal('blockchain')" class="w-full py-3 px-4 bg-white/5 text-white/80 rounded-xl border border-white/10 font-bold text-right flex items-center justify-between hover:bg-heritage-neonBlue hover:text-black transition-all">
                <span class="text-sm">٧. العقود الذكية (بلوك تشين)</span>
                <span class="text-lg">⛓️</span>
            </button>

            <!-- 8. لوحة التحكم -->
            <button onclick="toggleAdmin();" class="w-full py-3 px-4 bg-heritage-neonBlue/10 text-heritage-neonBlue rounded-xl border border-heritage-neonBlue/20 font-bold text-right flex items-center justify-between hover:bg-heritage-neonBlue hover:text-black transition-all">
                <span class="text-sm">٨. لوحة التحكم</span>
                <span class="text-lg">⚙️</span>
            </button>

            <!-- 9. الكتب والمراجع -->
            <button onclick="openInfoModal('books')" class="w-full py-3 px-4 bg-white/5 text-white/80 rounded-xl border border-white/10 font-bold text-right flex items-center justify-between hover:bg-heritage-neonBlue hover:text-black transition-all">
                <span class="text-sm">٩. الكتب والمراجع</span>
                <span class="text-lg">📚</span>
            </button>

            <!-- 10. المناسبات والأحداث -->
            <button onclick="openInfoModal('events')" class="w-full py-3 px-4 bg-white/5 text-white/80 rounded-xl border border-white/10 font-bold text-right flex items-center justify-between hover:bg-heritage-neonBlue hover:text-black transition-all">
                <span class="text-sm">١٠. المناسبات والأحداث</span>
                <span class="text-lg">📅</span>
            </button>

            <!-- 11. الصور والفيديوهات -->
            <button onclick="openInfoModal('media')" class="w-full py-3 px-4 bg-white/5 text-white/80 rounded-xl border border-white/10 font-bold text-right flex items-center justify-between hover:bg-heritage-neonBlue hover:text-black transition-all">
                <span class="text-sm">١١. الصور والفيديوهات</span>
                <span class="text-lg">🎥</span>
            </button>

            <!-- 12. التحقق الرسمي -->
            <button onclick="openInfoModal('verify')" class="w-full py-3 px-4 bg-white/5 text-white/80 rounded-xl border border-white/10 font-bold text-right flex items-center justify-between hover:bg-heritage-neonBlue hover:text-black transition-all">
                <span class="text-sm">١٢. التحقق الرسمي</span>
                <span class="text-lg">🛡️</span>
            </button>

            <!-- 13. اللغة -->
            <button onclick="openInfoModal('lang')" class="w-full py-3 px-4 bg-white/5 text-white/80 rounded-xl border border-white/10 font-bold text-right flex items-center justify-between hover:bg-heritage-neonBlue hover:text-black transition-all">
                <span class="text-sm">١٣. اللغة</span>
                <span class="text-lg">🌐</span>
            </button>

            <!-- 14. الوضع الليلي/النهاري -->
            <button onclick="toggleTheme();" class="w-full py-3 px-4 bg-white/5 text-white/80 rounded-xl border border-white/10 font-bold text-right flex items-center justify-between hover:bg-heritage-neonBlue hover:text-black transition-all">
                <span class="text-sm">١٤. الوضع الليلي/النهاري</span>
                <span class="text-lg">🌓</span>
            </button>

            <!-- 15. حول المنصة -->
            <button onclick="openInfoModal('about')" class="w-full py-3 px-4 bg-white/5 text-white/80 rounded-xl border border-white/10 font-bold text-right flex items-center justify-between hover:bg-heritage-neonBlue hover:text-black transition-all">
                <span class="text-sm">١٥. حول المنصة</span>
                <span class="text-lg">ℹ️</span>
            </button>

            <!-- 16. المكافآت والهدايا -->
            <button onclick="openInfoModal('rewards')" class="w-full py-3 px-4 bg-white/5 text-white/80 rounded-xl border border-white/10 font-bold text-right flex items-center justify-between hover:bg-heritage-neonBlue hover:text-black transition-all">
                <span class="text-sm">١٦. المكافآت والهدايا</span>
                <span class="text-lg">🎁</span>
            </button>
    """
    # Replace the whole list for simplicity
    regex_sidebar = r'<div class="w-full space-y-2">.*?</div>\s*<div class="mt-12'
    replacement = '<div class="w-full space-y-2">' + sidebar_html + '</div>\n\n        <div class="mt-12'
    content = re.sub(regex_sidebar, replacement, content, flags=re.DOTALL)

# 3. Add Tree Modal HTML before Map Modal
if 'id="treeModal"' not in content:
    tree_modal_html = """
    <!-- 3D Tree Modal -->
    <div id="treeModal" class="fixed inset-0 bg-black/95 backdrop-blur-3xl z-[300] hidden items-center justify-center p-4">
        <div class="max-w-6xl w-full h-[90vh] glass-effect rounded-[4rem] p-10 border border-heritage-gold/30 relative flex flex-col overflow-hidden">
            <button onclick="closeTree()" class="absolute top-10 left-10 text-heritage-gold/40 hover:text-heritage-gold transition-all z-20">
                 <svg xmlns="http://www.w3.org/2000/svg" class="h-10 w-10" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M6 18L18 6M6 6l12 12" />
                </svg>
            </button>
            <div class="mb-6 flex justify-between items-end relative z-10">
                <div>
                    <h2 class="text-4xl font-black text-heritage-gold">شجرة النسب الرقمية (3D)</h2>
                    <p class="text-xs font-bold opacity-40 uppercase tracking-widest">تجسيد تفاعلي لسلالة قبيلة الحياني</p>
                </div>
                <div class="flex gap-2">
                    <button onclick="initLivingTree()" class="px-6 py-2 bg-heritage-gold/10 text-heritage-gold rounded-full text-[10px] font-black border border-heritage-gold/20">تحديث الشجرة 🔄</button>
                </div>
            </div>
            <div id="tree-3d-container" class="flex-grow bg-black/20 rounded-[3rem] border border-white/5 relative cursor-move">
                <div id="node-info-label" class="node-label"></div>
            </div>
            <div class="mt-6 flex justify-between text-[10px] font-bold opacity-40 uppercase tracking-widest relative z-10">
                <span>Touch to rotate / Scroll to zoom</span>
                <span>Powered by Three.js & Diwan AI</span>
            </div>
        </div>
    </div>
"""
    content = content.replace('<!-- Interactive Map Modal -->', tree_modal_html + '\n    <!-- Interactive Map Modal -->')

# 4. Add JavaScript functions
if 'function openTree()' not in content:
    js_funcs = """
        function openTree() {
            closePanels();
            document.getElementById('treeModal').classList.remove('hidden');
            document.getElementById('treeModal').classList.add('flex');
            document.getElementById('overlay').classList.remove('hidden');
            initLivingTree();
        }

        function closeTree() {
            document.getElementById('treeModal').classList.add('hidden');
            document.getElementById('treeModal').classList.remove('flex');
            if (document.getElementById('adminPanel').classList.contains('hidden')) {
                document.getElementById('overlay').classList.add('hidden');
            }
            if(window.treeAnimationId) cancelAnimationFrame(window.treeAnimationId);
        }

        function initLivingTree() {
            const container = document.getElementById('tree-3d-container');
            if(!container) return;
            container.innerHTML = '<div id="node-info-label" class="node-label"></div>';

            const width = container.clientWidth;
            const height = container.clientHeight;

            const scene = new THREE.Scene();
            const camera = new THREE.PerspectiveCamera(75, width / height, 0.1, 1000);
            const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
            renderer.setSize(width, height);
            container.appendChild(renderer.domElement);

            // Lighting
            const ambientLight = new THREE.AmbientLight(0xffffff, 0.5);
            scene.add(ambientLight);
            const pointLight = new THREE.PointLight(0x00f2ff, 1);
            pointLight.position.set(10, 10, 10);
            scene.add(pointLight);

            const nodes = [];
            const connections = [];

            // Create a stylized tree structure based on vault data
            const treeData = vault.slice(0, 15); // Show first 15 for performance

            // Genesis Node
            const genesisGeo = new THREE.SphereGeometry(0.8, 32, 32);
            const genesisMat = new THREE.MeshPhongMaterial({ color: 0xd4af37, emissive: 0xd4af37, emissiveIntensity: 0.5 });
            const genesisNode = new THREE.Mesh(genesisGeo, genesisMat);
            genesisNode.position.set(0, 0, 0);
            genesisNode.userData = { name: "موسى الجون (الجد الجامع)", info: "سلالة الهاشميين" };
            scene.add(genesisNode);
            nodes.push(genesisNode);

            // Child Nodes
            treeData.forEach((m, i) => {
                const angle = (i / treeData.length) * Math.PI * 2;
                const radius = 5 + Math.random() * 2;
                const x = Math.cos(angle) * radius;
                const y = (Math.random() - 0.5) * 4;
                const z = Math.sin(angle) * radius;

                const geo = new THREE.SphereGeometry(0.4, 16, 16);
                const mat = new THREE.MeshPhongMaterial({ color: 0x00f2ff });
                const node = new THREE.Mesh(geo, mat);
                node.position.set(x, y, z);
                node.userData = { name: m.name, info: m.id };
                scene.add(node);
                nodes.push(node);

                // Connection line
                const points = [new THREE.Vector3(0,0,0), new THREE.Vector3(x,y,z)];
                const lineGeo = new THREE.BufferGeometry().setFromPoints(points);
                const lineMat = new THREE.LineBasicMaterial({ color: 0x00f2ff, transparent: true, opacity: 0.2 });
                const line = new THREE.Line(lineGeo, lineMat);
                scene.add(line);
                connections.push(line);
            });

            camera.position.z = 12;

            // Interaction
            const raycaster = new THREE.Raycaster();
            const mouse = new THREE.Vector2();
            const label = document.getElementById('node-info-label');

            container.onmousemove = (e) => {
                const rect = container.getBoundingClientRect();
                mouse.x = ((e.clientX - rect.left) / width) * 2 - 1;
                mouse.y = -((e.clientY - rect.top) / height) * 2 + 1;

                raycaster.setFromCamera(mouse, camera);
                const intersects = raycaster.intersectObjects(nodes);

                nodes.forEach(n => n.scale.set(1, 1, 1));
                label.style.display = 'none';
                label.classList.remove('selected-label');

                if (intersects.length > 0) {
                    const obj = intersects[0].object;
                    obj.scale.set(1.5, 1.5, 1.5);
                    label.style.display = 'block';
                    label.classList.add('selected-label');
                    label.innerText = obj.userData.name;
                    label.style.left = (e.clientX - rect.left) + 'px';
                    label.style.top = (e.clientY - rect.top) + 'px';
                }
            };

            let rotationY = 0;
            const animate = () => {
                window.treeAnimationId = requestAnimationFrame(animate);
                rotationY += 0.005;
                scene.rotation.y = rotationY;

                nodes.forEach((n, i) => {
                    if(i > 0) n.position.y += Math.sin(Date.now() * 0.001 + i) * 0.01;
                });

                renderer.render(scene, camera);
            };
            animate();
        }
"""
    content = content.replace('function closeMap() {', js_funcs + '\n        function closeMap() {')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
