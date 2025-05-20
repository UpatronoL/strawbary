document.addEventListener('DOMContentLoaded', () => {
    console.log('Language switcher script loaded');
  
    const translations = {
      en: {
        // Base.html
        title: 'My Website',
        'nav-home': 'Home',
        'nav-measurements': 'Measurements',
        'nav-summary': 'Summary',
        'nav-analysis': 'Analysis',
        footer: 'Footer content',
  
        // Home.html
        'hero-title': 'Strawberry Farm Innovation',
        'hero-subtitle': 'Revolutionizing premium strawberry cultivation through smart environmental sensing technology',
        'about-title': 'About the Project',
        'about-text': 'MIGAKI-ICHIGO represents the pinnacle of strawberry cultivation, and our project aims to push the boundaries further with cutting-edge monitoring technology.',
        'challenge-title': 'The Challenge',
        'challenge-text': 'Nursery greenhouses lack adequate monitoring systems, creating blind spots in the cultivation process that affect yield and quality.',
        'solution-title': 'Our Solution',
        'solution-text': 'Compact, wireless environmental sensors that provide real-time data on critical growth factors without disrupting operations.',
        'impact-title': 'The Impact',
        'impact-text': 'Increased yields, improved quality, and data-driven decision making for strawberry farmers.',
        'tech-title': 'Technical Challenges',
        'wireless-title': 'Wireless Communication',
        'wireless-text': 'Overcoming steel structure interference to maintain reliable data transmission up to 2km.',
        'durability-title': 'Durability',
        'durability-text': 'Creating waterproof housings that withstand harsh greenhouse conditions.',
        'data-title': 'Data Integrity',
        'data-text': 'Ensuring continuous monitoring with offline data retention capabilities.',
        'prototype-title': 'Our Prototype',
        'prototype-text': 'The current iteration of our environmental sensing device blends seamlessly into strawberry seedling trays while collecting critical growth data.',
        'feature-1': 'Compact, unobtrusive design',
        'feature-2': 'Multi-sensor array',
        'feature-3': 'Long-range communication',
        'feature-4': 'Weather-resistant housing',
        'achievements-title': 'Expected Achievements',
        'achievements-text': 'By implementing our solution, we aim to increase strawberry yields by 20-30% while improving quality consistency and reducing resource waste.',
        'steps-title': 'Next Steps',
        'step1-title': 'Field Testing',
        'step1-text': 'Real-world validation in nursery environments',
        'step2-title': 'Algorithm Refinement',
        'step2-text': 'Enhancing data analysis for actionable insights',
        'step3-title': 'Farmer Interface',
        'step3-text': 'Developing intuitive dashboards',
        'step4-title': 'Communication Reliability',
        'step4-text': 'Ensuring robust long-distance transmission',
  
        // table.html
        filterByDate: 'Filter by date:',
        apply: 'Apply',
        showAll: 'Show All',
        filterValuePlaceholder: 'Filter Value',
        tableHeaders: [
          'Date', 'Time', 'Temperature', 'Humidity',
          'Light Intensity', 'Ground Temperature', 'Ground Humidity'
        ],
        summaryTitle: 'Temperature Summary',
        maxTemp: 'Max Temperature:',
        minTemp: 'Min Temperature:',
        meanTemp: 'Mean Temperature:',
        daytimeAvg: 'Daytime Average:',
        nighttimeAvg: 'Nighttime Average:',
        noData: 'No temperature data available.',
        downloadTitle: 'Click here 👇',
        downloadBtn: 'Download Data',
        searchPlaceholder: 'Search all columns...',
        lengthMenu: 'Show _MENU_ entries',
        info: 'Showing _START_ to _END_ of _TOTAL_ entries',
  
        // summary.html
        category: 'Category',
        metric: 'Metric',
        categories: {
          temperature: 'Temperature (°C)',
          humidity: 'Humidity (%)',
          light: 'Light Intensity',
          groundTemp: 'Ground Temperature (°C)',
          groundHumidity: 'Ground Humidity (%)'
        },
        metrics: {
          max: 'Max',
          min: 'Min',
          dailyAvg: 'Daily Avg',
          daytimeAvg: 'Daytime Avg',
          nighttimeAvg: 'Nighttime Avg'
        },
  
        // Analysis page
        'analysis-daily-title':       'Daily Environmental Data Analysis',
        'analysis-weekly-title':      'Weekly Environmental Data Analysis',
        'analysis-temp':              'Temperature',
        'analysis-humidity':          'Humidity',
        'analysis-light':             'Light Intensity',
        'analysis-day-avg-temp':      'Daytime Average Temperature',
        'analysis-day-avg-humidity':  'Daytime Average Humidity',
        'analysis-day-avg-light':     'Daytime Average Light Intensity',
        'analysis-night-avg-temp':    'Nighttime Average Temperature',
        'analysis-night-avg-humidity':'Nighttime Average Humidity',
        'analysis-night-avg-light':   'Nighttime Average Light Intensity',
        'analysis-whole-avg-temp':    'Whole-Day Average Temperature',
        'analysis-whole-avg-humidity':'Whole-Day Average Humidity',
        'analysis-whole-avg-light':   'Whole-Day Average Light Intensity',
        'modal-close':                '×'
      },
      ja: {
        // Base.html
        title: '私のウェブサイト',
        'nav-home': 'ホーム',
        'nav-measurements': '測定',
        'nav-summary': '概要',
        'nav-analysis': '分析',
        footer: 'フッターコンテンツ',
  
        // Home.html
        'hero-title': 'イチゴ農園の革新',
        'hero-subtitle': 'スマート環境センシング技術による高級イチゴ栽培の革新',
        'about-title': 'プロジェクトについて',
        'about-text': 'ミガキイチゴはイチゴ栽培の頂点を表し、私たちのプロジェクトは最先端の監視技術でその限界をさらに押し広げることを目指しています。',
        'challenge-title': '課題',
        'challenge-text': '育苗用温室には適切な監視システムが不足しており、収量と品質に影響を与える栽培プロセスの盲点が生じています。',
        'solution-title': '私たちの解決策',
        'solution-text': '作業を妨げることなく重要な成長要因に関するリアルタイムデータを提供するコンパクトな無線環境センサー。',
        'impact-title': '影響',
        'impact-text': 'イチゴ農家の収量増加、品質向上、データに基づく意思決定。',
        'tech-title': '技術的課題',
        'wireless-title': '無線通信',
        'wireless-text': '鋼構造物の干渉を克服し、2kmまでの信頼性のあるデータ伝送を維持。',
        'durability-title': '耐久性',
        'durability-text': '過酷な温室条件に耐える防水ケースの作成。',
        'data-title': 'データの完全性',
        'data-text': 'オフライン時のデータ保持機能を備えた継続的な監視の確保。',
        'prototype-title': '私たちのプロトタイプ',
        'prototype-text': '現在の環境センシングデバイスの反復は、重要な成長データを収集しながら、イチゴの苗トレイにシームレスに溶け込みます。',
        'feature-1': 'コンパクトで目立たないデザイン',
        'feature-2': 'マルチセンサーアレイ',
        'feature-3': '長距離通信',
        'feature-4': '耐候性ハウジング',
        'achievements-title': '期待される成果',
        'achievements-text': '私たちのソリューションを実装することで、イチゴの収量を20-30％増加させ、品質の一貫性を向上させ、資源の浪費を減らすことを目指しています。',
        'steps-title': '次のステップ',
        'step1-title': 'フィールドテスト',
        'step1-text': '育苗環境での実世界での検証',
        'step2-title': 'アルゴリズムの改良',
        'step2-text': '実用的な洞察のためのデータ分析の強化',
        'step3-title': '農家向けインターフェース',
        'step3-text': '直感的なダッシュボードの開発',
        'step4-title': '通信の信頼性',
        'step4-text': '堅牢な長距離伝送の確保',
  
        // table.html
        filterByDate: '日付でフィルター:',
        apply: '適用',
        showAll: 'すべて表示',
        filterValuePlaceholder: 'フィルター値',
        tableHeaders: [
          '日付', '時間', '温度', '湿度',
          '光の強さ', '地温', '地中湿度'
        ],
        summaryTitle: '温度の概要',
        maxTemp: '最高温度:',
        minTemp: '最低温度:',
        meanTemp: '平均温度:',
        daytimeAvg: '日中の平均:',
        nighttimeAvg: '夜間の平均:',
        noData: '温度データはありません。',
        downloadTitle: 'こちらをクリック 👇',
        downloadBtn: 'データをダウンロード',
        searchPlaceholder: 'すべての列を検索...',
        lengthMenu: '_MENU_ 件を表示',
        info: '_TOTAL_ 件中 _START_ から _END_ を表示',
  
        // summary.html
        category: 'カテゴリ',
        metric: '指標',
        categories: {
          temperature: '気温 (°C)',
          humidity: '湿度 (%)',
          light: '光の強さ',
          groundTemp: '地温 (°C)',
          groundHumidity: '地中湿度 (%)'
        },
        metrics: {
          max: '最大',
          min: '最小',
          dailyAvg: '1日平均',
          daytimeAvg: '日中平均',
          nighttimeAvg: '夜間平均'
        },
  
        // Analysis page
        'analysis-daily-title':       '日次環境データ分析',
        'analysis-weekly-title':      '週次環境データ分析',
        'analysis-temp':              '温度',
        'analysis-humidity':          '湿度',
        'analysis-light':             '光の強さ',
        'analysis-day-avg-temp':      '日中平均温度',
        'analysis-day-avg-humidity':  '日中平均湿度',
        'analysis-day-avg-light':     '日中平均光強度',
        'analysis-night-avg-temp':    '夜間平均温度',
        'analysis-night-avg-humidity':'夜間平均湿度',
        'analysis-night-avg-light':   '夜間平均光強度',
        'analysis-whole-avg-temp':    '全日平均温度',
        'analysis-whole-avg-humidity':'全日平均湿度',
        'analysis-whole-avg-light':   '全日平均光強度',
        'modal-close':                '×'
      }
    };
  
    const languageSelect = document.getElementById('language-select')
      || document.querySelector('.language-selector select');
  
    if (!languageSelect) {
      console.error('Language select element not found');
      return;
    }
  
    

    const savedLang = localStorage.getItem('preferredLanguage') || 'en';
    languageSelect.value = savedLang;
    setLanguage(savedLang);
  
    languageSelect.addEventListener('change', e => {
      const lang = e.target.value;
      console.log(`Language changed to: ${lang}`);
      localStorage.setItem('preferredLanguage', lang);
      setLanguage(lang);
    });
  
    function setLanguage(lang) {
      console.group(`Updating language to ${lang}`);
      document.documentElement.lang = lang;
      const dict = translations[lang] || translations.en;
  
      // Update textContent and placeholders
      Object.entries(dict).forEach(([key, value]) => {
        document.querySelectorAll(`[data-i18n="${key}"]`)
          .forEach(el => {
            if (el.tagName === 'INPUT' && el.placeholder !== undefined) {
              el.placeholder = value;
            } else {
              el.textContent = value;
            }
          });
  
        // Update alt attributes on images
        document.querySelectorAll(`[data-i18n-alt="${key}"]`)
          .forEach(img => {
            img.alt = value;
          });
      });
  
      // Update <title> tag
      if (dict.title) {
        document.title = dict.title;
      }
      console.groupEnd();
    }
  });