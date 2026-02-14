from flask import Flask, render_template_string

app = Flask(__name__)

html = """
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>聂灏宇</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            background: #f2f2f2;
            padding: 20px;
            font-family: Arial, sans-serif;
            position: relative;
        }
        .title {
            text-align: center;
            margin-bottom: 30px;
            color: #333;
        }
        .box {
            background: white;
            border-radius: 12px;
            padding: 15px;
            margin-bottom: 20px;
            box-shadow: 0 2px 8px #00000010;
        }
        .box h3 {
            margin-bottom: 10px;
            color: #ff4081;
        }
        .links {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
        }
        a {
            padding: 10px 14px;
            background: #e3f2fd;
            border-radius: 8px;
            text-decoration: none;
            color: #0d47a1;
            font-weight: bold;
            transition: all 0.2s;
        }
        a:hover {
            background: #bbdefb;
            transform: scale(1.05);
        }
        /* 罗布乐思人物样式 */
        .roblox-char {
            position: fixed;
            bottom: 20px;
            right: 20px;
            width: 120px;
            height: auto;
            z-index: 999;
            cursor: pointer;
        }
        /* 弹窗样式 */
        .popup {
            display: none;
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background: white;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0 4px 16px rgba(0,0,0,0.2);
            z-index: 1000;
            text-align: center;
        }
        .popup h2 {
            color: #ff4081;
            margin-bottom: 15px;
        }
        .popup button {
            padding: 8px 16px;
            background: #0d47a1;
            color: white;
            border: none;
            border-radius: 8px;
            cursor: pointer;
        }
    </style>
</head>
<body>

    <h1 class="title">😎😎</h1>

    <div class="box">
        <h3>🎬 短视频🤩</h3>
        <div class="links">
            <a href="https://www.douyin.com" target="_blank" class="site-link">抖音</a>
            <a href="https://www.kuaishou.com" target="_blank" class="site-link">快手</a>
            <a href="https://www.bilibili.com" target="_blank" class="site-link">B站</a>
            <a href="https://www.xiaohongshu.com" target="_blank" class="site-link">小红书</a>
            <a href="https://weibo.com" target="_blank" class="site-link">微博</a>
        </div>
    </div>

    <div class="box">
        <h3>📰 新闻资讯🧐</h3>
        <div class="links">
            <a href="https://www.baidu.com" target="_blank" class="site-link">百度</a>
            <a href="https://www.sogou.com" target="_blank" class="site-link">搜狗</a>
            <a href="https://www.163.com" target="_blank" class="site-link">网易</a>
            <a href="https://www.qq.com" target="_blank" class="site-link">腾讯</a>
        </div>
    </div>

    <div class="box">
        <h3>📖 免费小说</h3>
        <div class="links">
            <a href="https://www.qidian.com" target="_blank" class="site-link">起点</a>
            <a href="https://www.biquge.com.ru" target="_blank" class="site-link">笔趣阁</a>
            <a href="https://www.biquge7.com" target="_blank" class="site-link">笔趣阁7</a>
            <a href="https://www.biquge.biz" target="_blank" class="site-link">笔趣阁备用</a>
        </div>
    </div>

    <div class="box">
        <h3>🎵 音乐</h3>
        <div class="links">
            <a href="https://music.163.com" target="_blank" class="site-link">网易云</a>
            <a href="https://y.qq.com" target="_blank" class="site-link">QQ音乐</a>
            <a href="https://music.kugou.com" target="_blank" class="site-link">酷狗</a>
        </div>
    </div>

    <div class="box">
        <h3>🎬 影视</h3>
        <div class="links">
            <a href="https://v.qq.com" target="_blank" class="site-link">腾讯视频</a>
            <a href="https://www.iqiyi.com" target="_blank" class="site-link">爱奇艺</a>
            <a href="https://youku.com" target="_blank" class="site-link">优酷</a>
        </div>
    </div>

    <!-- 罗布乐思人物 -->
    <img src="https://www.roblox.com/headshot-thumbnail/image?userId=1&width=420&height=420&format=png">

    <!-- 弹窗 -->
    <div class="popup" id="successPopup">
        <h2>🎉 耶！</h2>
        <p>你已成功进入网站！</p>
        <button onclick="closePopup()">确定</button>
    </div>

    <script>
        // 罗布乐思笑声（用Web Audio API模拟）
        function playRobloxSound() {
            const audioCtx = new (window.AudioContext || window.webkitAudioContext)();
            const oscillator = audioCtx.createOscillator();
            const gainNode = audioCtx.createGain();
            
            oscillator.connect(gainNode);
            gainNode.connect(audioCtx.destination);
            
            oscillator.type = 'square';
            oscillator.frequency.setValueAtTime(440, audioCtx.currentTime);
            oscillator.frequency.setValueAtTime(880, audioCtx.currentTime + 0.1);
            oscillator.frequency.setValueAtTime(440, audioCtx.currentTime + 0.2);
            
            gainNode.gain.setValueAtTime(0.3, audioCtx.currentTime);
            gainNode.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.5);
            
            oscillator.start(audioCtx.currentTime);
            oscillator.stop(audioCtx.currentTime + 0.5);
        }

        // 弹窗控制
        function showPopup(siteName) {
            playRobloxSound();
            const popup = document.getElementById('successPopup');
            popup.querySelector('p').textContent = `你已成功进入${siteName}！`;
            popup.style.display = 'block';
        }

        function closePopup() {
            document.getElementById('successPopup').style.display = 'none';
        }

        // 绑定网站链接点击事件
        document.querySelectorAll('.site-link').forEach(link => {
            link.addEventListener('click', function(e) {
                const siteName = this.textContent;
                showPopup(siteName);
                // 延迟跳转，让音效和弹窗先显示
                setTimeout(() => {
                    window.open(this.href, '_blank');
                }, 600);
                e.preventDefault();
            });
        });
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(html)

if __name__ == '__main__':
    print("✅ 导航网站已启动！")
    print("👉 打开浏览器访问：http://127.0.0.1:5000")
    app.run(host='0.0.0.0', port=5000, debug=False)
    