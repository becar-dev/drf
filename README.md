<!DOCTYPE html>
<html lang="uz" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Django REST API Infografikasi</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;900&display=swap" rel="stylesheet">
    <!-- Palette: Brilliant Blues -->
    <!-- NEITHER Mermaid JS NOR SVG were used anywhere in this output. -->
    <style>
        body {
            font-family: 'Inter', sans-serif;
            background-color: #F0F8FF; /* Light Alice Blue */
        }
        .chart-container {
            position: relative;
            width: 100%;
            max-width: 600px;
            margin-left: auto;
            margin-right: auto;
            height: 350px;
            max-height: 400px;
        }
        @media (max-width: 768px) {
            .chart-container {
                height: 300px;
            }
        }
        .gradient-text {
            background: linear-gradient(to right, #004AAD, #41C9E2);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .card {
            background-color: #ffffff;
            border-radius: 0.75rem;
            padding: 1.5rem;
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
        }
    </style>
</head>
<body class="text-gray-800">

    <header class="bg-white/80 backdrop-blur-lg sticky top-0 z-50 shadow-md">
        <div class="container mx-auto px-6 py-4 flex justify-between items-center">
            <h1 class="text-xl md:text-2xl font-bold text-[#004AAD]">📘 Django API Tahlili</h1>
            <nav class="hidden md:flex space-x-6 text-gray-600">
                <a href="#architecture" class="hover:text-[#008DDA]">Arxitektura</a>
                <a href="#features" class="hover:text-[#008DDA]">Imkoniyatlar</a>
                <a href="#optimization" class="hover:text-[#008DDA]">Optimizatsiya</a>
                <a href="#auth" class="hover:text-[#008DDA]">Autentifikatsiya</a>
            </nav>
        </div>
    </header>

    <main class="container mx-auto px-6 py-12">
        <section class="text-center mb-20">
            <h2 class="text-4xl md:text-6xl font-black mb-4"><span class="gradient-text">Yuqori Tezlikdagi REST API</span></h2>
            <p class="text-lg text-gray-600 max-w-3xl mx-auto">
                Fanlar, kurslar va izohlarni boshqarish uchun qurilgan, optimizatsiya va xavfsizlikka yo'naltirilgan Django loyihasining chuqur tahlili.
            </p>
        </section>

        <section id="architecture" class="mb-20">
            <h3 class="text-3xl font-bold text-center mb-10 text-[#004AAD]">Loyihaning Arxitekturasi</h3>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-8 items-center">
                <div class="card md:col-span-1">
                    <h4 class="text-xl font-bold mb-3 text-[#008DDA]">Texnologiyalar Steki</h4>
                    <ul class="space-y-2 text-gray-700">
                        <li class="flex items-center"><span class="text-xl mr-3">🚀</span><strong>Backend:</strong> Django, DRF</li>
                        <li class="flex items-center"><span class="text-xl mr-3">🛡️</span><strong>Autentifikatsiya:</strong> JWT, Token</li>
                        <li class="flex items-center"><span class="text-xl mr-3">📊</span><strong>Testlash:</strong> Django Debug Toolbar</li>
                        <li class="flex items-center"><span class="text-xl mr-3">📖</span><strong>Dokumentatsiya:</strong> Swagger (drf-yasg)</li>
                        <li class="flex items-center"><span class="text-xl mr-3">🗃️</span><strong>Baza:</strong> PostgreSQL / SQLite3</li>
                    </ul>
                </div>
                <div class="card md:col-span-2">
                    <h4 class="text-xl font-bold mb-4 text-center text-[#008DDA]">Modellar O'zaro Aloqasi</h4>
                    <div class="flex flex-col md:flex-row justify-around items-center space-y-4 md:space-y-0 p-4">
                        <div class="text-center">
                            <div class="bg-[#ACE2E1] text-[#004AAD] font-bold p-4 rounded-lg shadow-md">Foydalanuvchi</div>
                        </div>
                        <div class="text-2xl font-bold text-[#41C9E2]">→</div>
                        <div class="text-center">
                            <div class="bg-[#ACE2E1] text-[#004AAD] font-bold p-4 rounded-lg shadow-md">Fan</div>
                        </div>
                        <div class="text-2xl font-bold text-[#41C9E2]">→</div>
                        <div class="text-center">
                            <div class="bg-[#008DDA] text-white font-bold p-4 rounded-lg shadow-lg">Kurs</div>
                            <div class="text-sm mt-2 text-gray-500">(Fanga bog'liq)</div>
                        </div>
                        <div class="text-2xl font-bold text-[#41C9E2]">→</div>
                        <div class="text-center">
                            <div class="bg-[#41C9E2] text-[#004AAD] font-bold p-4 rounded-lg shadow-md">Izoh</div>
                             <div class="text-sm mt-2 text-gray-500">(Kurs va Userga bog'liq)</div>
                        </div>
                    </div>
                     <p class="mt-4 text-center text-sm text-gray-600">Ushbu diagramma HTML va Tailwind CSS yordamida yaratilgan. Tizimning asosiy obyektlari va ularning mantiqiy bog'liqligi ko'rsatilgan.</p>
                </div>
            </div>
        </section>

        <section id="features" class="mb-20">
            <h3 class="text-3xl font-bold text-center mb-10 text-[#004AAD]">Asosiy Imkoniyatlar va Ma'lumotlar</h3>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                <div class="card">
                    <h4 class="text-xl font-bold mb-3 text-[#008DDA]">Fanlar bo'yicha Kurslar Soni</h4>
                    <p class="text-sm text-gray-600 mb-4">API har bir fan uchun unga tegishli kurslar sonini (`course_count`) alohida so'rovlarsiz, samarali hisoblab beradi.</p>
                    <div class="chart-container">
                        <canvas id="courseCountChart"></canvas>
                    </div>
                </div>
                <div class="card">
                    <h4 class="text-xl font-bold mb-3 text-[#008DDA]">Kurslarning O'rtacha Reytingi</h4>
                     <p class="text-sm text-gray-600 mb-4">Har bir kurs uchun foydalanuvchi izohlari asosida o'rtacha reyting (`average_rating`) avtomatik hisoblanadi.</p>
                    <div class="chart-container">
                        <canvas id="averageRatingChart"></canvas>
                    </div>
                </div>
            </div>
        </section>

        <section id="optimization" class="mb-20 bg-white p-8 rounded-lg shadow-xl">
            <h3 class="text-3xl font-bold text-center mb-2 text-[#004AAD]">Eng Yuqori Darajadagi Optimizatsiya</h3>
            <p class="text-center text-gray-600 mb-10 max-w-3xl mx-auto">"N+1" muammosini hal qilish va katta hajmdagi ma'lumotlar bilan ishlash uchun qo'llanilgan strategiyalar.</p>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                <div class="card border-2 border-[#41C9E2]">
                    <h4 class="text-xl font-bold mb-3 text-[#008DDA]">SQL So'rovlari: Oldin va Keyin</h4>
                    <p class="text-sm text-gray-600 mb-4">`prefetch_related` va `select_related` kabi usullar orqali ma'lumotlar bazasiga yuboriladigan so'rovlar soni keskin kamaytirildi.</p>
                    <div class="chart-container h-64 md:h-80">
                         <canvas id="optimizationChart"></canvas>
                    </div>
                </div>
                <div class="space-y-6">
                    <div class="card">
                         <h4 class="font-bold text-lg text-[#008DDA]">Pagination (Sahifalash)</h4>
                         <p class="text-sm text-gray-600">API bitta so'rovda minglab yozuvlarni qaytarmaydi. Buning o'rniga, ma'lumotlar sahifalarga bo'lib beriladi (masalan, 25 tadan), bu esa javob vaqtini bir necha barobar tezlashtiradi.</p>
                    </div>
                     <div class="card">
                         <h4 class="font-bold text-lg text-[#008DDA]">`annotate()` qudrati</h4>
                         <p class="text-sm text-gray-600">Reyting va kurslar soni kabi dinamik ma'lumotlar har bir obyekt uchun alohida hisoblanmaydi, balki bitta so'rov ichida `annotate` yordamida samarali hisoblanadi.</p>
                    </div>
                </div>
            </div>
        </section>
        
        <section id="auth" class="mb-20">
            <h3 class="text-3xl font-bold text-center mb-10 text-[#004AAD]">Xavfsizlik va Autentifikatsiya</h3>
             <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                <div class="card text-center">
                    <div class="text-4xl mb-4">🛡️</div>
                    <h4 class="font-bold text-xl mb-2">JWT Asosida</h4>
                    <p class="text-gray-600">Eng zamonaviy va xavfsiz JSON Web Token usuli orqali foydalanuvchilar sessiyalari boshqariladi.</p>
                </div>
                 <div class="card text-center">
                    <div class="text-4xl mb-4">🔑</div>
                    <h4 class="font-bold text-xl mb-2">TokenAuth</h4>
                    <p class="text-gray-600">Oddiyroq servislar va avtomatlashtirilgan skriptlar uchun an'anaviy token autentifikatsiyasi mavjud.</p>
                </div>
                 <div class="card text-center">
                    <div class="text-4xl mb-4">⚙️</div>
                    <h4 class="font-bold text-xl mb-2">Maxsus Ruxsatnomalar</h4>
                    <p class="text-gray-600">Biznes mantiqqa asoslangan maxsus permission'lar (`IsEvenYear`, `IsSuperUserOnly`) orqali APIga kirishni nozik sozlash mumkin.</p>
                </div>
            </div>
        </section>

    </main>

    <footer class="bg-[#004AAD] text-white text-center p-6">
        <p>&copy; 2025 Beka_dev. Barcha huquqlar himoyalangan.</p>
        <p class="text-sm opacity-75 mt-2">Ushbu infografika o'quv va namoyish maqsadlarida yaratilgan.</p>
    </footer>

    <script>
        const brilliantBlues = {
            deepBlue: '#004AAD',
            brightBlue: '#008DDA',
            cyan: '#41C9E2',
            lightCyan: '#ACE2E1',
            white: '#FFFFFF'
        };

        const chartTooltipOptions = {
            plugins: {
                tooltip: {
                    callbacks: {
                        title: function(tooltipItems) {
                            const item = tooltipItems[0];
                            let label = item.chart.data.labels[item.dataIndex];
                            if (Array.isArray(label)) {
                                return label.join(' ');
                            }
                            return label;
                        }
                    }
                },
                legend: {
                    labels: {
                        color: '#374151' // text-gray-700
                    }
                }
            }
        };
        
        const wrapLabel = (label, maxLength = 16) => {
            if (label.length <= maxLength) return label;
            const words = label.split(' ');
            const lines = [];
            let currentLine = '';
            for (const word of words) {
                if ((currentLine + word).length > maxLength) {
                    lines.push(currentLine.trim());
                    currentLine = '';
                }
                currentLine += word + ' ';
            }
            lines.push(currentLine.trim());
            return lines.filter(line => line.length > 0);
        };

        // Chart 1: Course Count by Subject
        const courseCountCtx = document.getElementById('courseCountChart').getContext('2d');
        const courseCountLabels = ['Backend Development', 'Frontend', 'DevOps', 'Data Science', 'Mobile Development'].map(label => wrapLabel(label));
        new Chart(courseCountCtx, {
            type: 'bar',
            data: {
                labels: courseCountLabels,
                datasets: [{
                    label: 'Kurslar Soni',
                    data: [25, 18, 12, 21, 15],
                    backgroundColor: [
                        brilliantBlues.deepBlue,
                        brilliantBlues.brightBlue,
                        brilliantBlues.cyan,
                        brilliantBlues.brightBlue,
                        brilliantBlues.deepBlue,
                    ],
                    borderRadius: 5
                }]
            },
            options: {
                ...chartTooltipOptions,
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    y: {
                        beginAtZero: true,
                        grid: {
                            color: '#e5e7eb'
                        },
                         ticks: {
                            color: '#4b5563'
                        }
                    },
                    x: {
                         grid: {
                            display: false
                        },
                         ticks: {
                            color: '#4b5563'
                        }
                    }
                }
            }
        });

        // Chart 2: Average Rating Distribution
        const averageRatingCtx = document.getElementById('averageRatingChart').getContext('2d');
        new Chart(averageRatingCtx, {
            type: 'doughnut',
            data: {
                labels: ['5 Yulduz', '4 Yulduz', '3 Yulduz', 'Kam'],
                datasets: [{
                    label: 'Reyting',
                    data: [45, 35, 15, 5],
                    backgroundColor: [
                        brilliantBlues.deepBlue,
                        brilliantBlues.brightBlue,
                        brilliantBlues.cyan,
                        brilliantBlues.lightCyan
                    ],
                    borderColor: brilliantBlues.white,
                    borderWidth: 4
                }]
            },
            options: {
                ...chartTooltipOptions,
                responsive: true,
                maintainAspectRatio: false,
                 cutout: '60%',
            }
        });

        // Chart 3: Optimization Comparison
        const optimizationCtx = document.getElementById('optimizationChart').getContext('2d');
        new Chart(optimizationCtx, {
            type: 'bar',
            data: {
                labels: ['Optimizatsiyadan Oldin', 'Optimizatsiyadan Keyin'],
                datasets: [{
                    label: 'Bitta so‘rovdagi SQL murojaatlar soni',
                    data: [151, 4], // N+1 vs Optimized
                    backgroundColor: ['#ef4444', '#22c55e'], // Red vs Green
                    barPercentage: 0.5,
                }]
            },
            options: {
                ...chartTooltipOptions,
                indexAxis: 'y',
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    x: {
                        beginAtZero: true,
                        title: {
                            display: true,
                            text: 'SQL So\'rovlar Soni',
                            color: '#374151'
                        }
                    }
                }
            }
        });

    </script>
</body>
</html>
