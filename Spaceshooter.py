import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Space Shooter", page_icon="🚀", layout="centered")

st.title("🚀 Space Shooter")
st.caption("Move with ← and →, shoot with spacebar. Survive and chase a high score.")

components.html(
    """
<!doctype html>
<html>
<head>
  <meta charset="utf-8" />
  <style>
    body {
      margin: 0;
      background: #070b1f;
      font-family: Arial, sans-serif;
      color: white;
      display: flex;
      justify-content: center;
    }
    #wrapper {
      width: 100%;
      max-width: 820px;
      padding: 10px 0;
    }
    #hud {
      display: flex;
      justify-content: space-between;
      font-size: 18px;
      margin: 8px 6px;
      letter-spacing: 0.5px;
    }
    #game {
      border: 2px solid #2e3c8a;
      border-radius: 10px;
      background: radial-gradient(circle at 50% 35%, #10183f, #050913 70%);
      box-shadow: 0 0 20px rgba(83, 137, 255, 0.35);
      width: 100%;
      max-width: 800px;
      height: 520px;
      display: block;
    }
    #help {
      margin: 10px 6px;
      color: #bec8ff;
      font-size: 14px;
    }
  </style>
</head>
<body>
  <div id="wrapper">
    <div id="hud">
      <span id="score">Score: 0</span>
      <span id="level">Level: 1</span>
      <span id="lives">Lives: 3</span>
    </div>
    <canvas id="game" width="800" height="520"></canvas>
    <div id="help">Tip: clear more enemies to increase the level and spawn rate.</div>
  </div>

  <script>
    const canvas = document.getElementById('game');
    const ctx = canvas.getContext('2d');

    const scoreEl = document.getElementById('score');
    const livesEl = document.getElementById('lives');
    const levelEl = document.getElementById('level');

    const keys = { ArrowLeft: false, ArrowRight: false, Space: false };

    const stars = Array.from({ length: 80 }, () => ({
      x: Math.random() * canvas.width,
      y: Math.random() * canvas.height,
      r: Math.random() * 1.8 + 0.2,
      speed: Math.random() * 0.7 + 0.3,
    }));

    const player = {
      x: canvas.width / 2,
      y: canvas.height - 45,
      width: 36,
      height: 24,
      speed: 6,
      cooldown: 0,
      lives: 3,
    };

    let bullets = [];
    let enemies = [];
    let particles = [];
    let score = 0;
    let level = 1;
    let defeated = 0;
    let gameOver = false;
    let spawnTick = 0;

    function resetGame() {
      bullets = [];
      enemies = [];
      particles = [];
      score = 0;
      level = 1;
      defeated = 0;
      spawnTick = 0;
      player.x = canvas.width / 2;
      player.lives = 3;
      player.cooldown = 0;
      gameOver = false;
      updateHud();
      requestAnimationFrame(loop);
    }

    function updateHud() {
      scoreEl.textContent = `Score: ${score}`;
      livesEl.textContent = `Lives: ${player.lives}`;
      levelEl.textContent = `Level: ${level}`;
    }

    function spawnEnemy() {
      const size = 26 + Math.random() * 16;
      enemies.push({
        x: Math.random() * (canvas.width - size),
        y: -size,
        size,
        speed: 1.2 + Math.random() * (1 + level * 0.25),
        zigzag: (Math.random() - 0.5) * 1.5,
        hue: 330 + Math.random() * 60,
      });
    }

    function shoot() {
      if (player.cooldown > 0 || gameOver) return;
      bullets.push({ x: player.x, y: player.y - player.height / 2, r: 3.5, speed: 8.5 });
      player.cooldown = 10;
    }

    function explode(x, y, color = '255,120,120') {
      for (let i = 0; i < 14; i++) {
        particles.push({
          x,
          y,
          vx: (Math.random() - 0.5) * 5,
          vy: (Math.random() - 0.5) * 5,
          life: 28 + Math.random() * 12,
          maxLife: 40,
          color,
        });
      }
    }

    function drawPlayer() {
      ctx.save();
      ctx.translate(player.x, player.y);

      ctx.fillStyle = '#69b8ff';
      ctx.beginPath();
      ctx.moveTo(0, -16);
      ctx.lineTo(16, 12);
      ctx.lineTo(6, 9);
      ctx.lineTo(0, 15);
      ctx.lineTo(-6, 9);
      ctx.lineTo(-16, 12);
      ctx.closePath();
      ctx.fill();

      ctx.fillStyle = '#d0ecff';
      ctx.beginPath();
      ctx.ellipse(0, 0, 4.5, 6.5, 0, 0, Math.PI * 2);
      ctx.fill();
      ctx.restore();
    }

    function drawEnemy(e) {
      ctx.fillStyle = `hsl(${e.hue}, 85%, 60%)`;
      ctx.beginPath();
      ctx.moveTo(e.x + e.size / 2, e.y);
      ctx.lineTo(e.x + e.size, e.y + e.size * 0.3);
      ctx.lineTo(e.x + e.size * 0.8, e.y + e.size);
      ctx.lineTo(e.x + e.size * 0.2, e.y + e.size);
      ctx.lineTo(e.x, e.y + e.size * 0.3);
      ctx.closePath();
      ctx.fill();
    }

    function drawStars() {
      for (const s of stars) {
        s.y += s.speed;
        if (s.y > canvas.height) {
          s.y = 0;
          s.x = Math.random() * canvas.width;
        }
        ctx.fillStyle = `rgba(220,230,255,${0.35 + s.r / 3})`;
        ctx.beginPath();
        ctx.arc(s.x, s.y, s.r, 0, Math.PI * 2);
        ctx.fill();
      }
    }

    function drawParticles() {
      for (let i = particles.length - 1; i >= 0; i--) {
        const p = particles[i];
        p.x += p.vx;
        p.y += p.vy;
        p.vx *= 0.97;
        p.vy *= 0.97;
        p.life -= 1;
        if (p.life <= 0) {
          particles.splice(i, 1);
          continue;
        }
        const alpha = p.life / p.maxLife;
        ctx.fillStyle = `rgba(${p.color},${alpha})`;
        ctx.fillRect(p.x, p.y, 3, 3);
      }
    }

    function update() {
      if (keys.ArrowLeft) player.x -= player.speed;
      if (keys.ArrowRight) player.x += player.speed;
      player.x = Math.max(player.width / 2, Math.min(canvas.width - player.width / 2, player.x));

      if (keys.Space) shoot();
      if (player.cooldown > 0) player.cooldown--;

      spawnTick++;
      const spawnRate = Math.max(18, 70 - level * 6);
      if (spawnTick >= spawnRate) {
        spawnEnemy();
        spawnTick = 0;
      }

      for (let i = bullets.length - 1; i >= 0; i--) {
        bullets[i].y -= bullets[i].speed;
        if (bullets[i].y < -10) bullets.splice(i, 1);
      }

      for (let i = enemies.length - 1; i >= 0; i--) {
        const e = enemies[i];
        e.y += e.speed;
        e.x += Math.sin(e.y / 24) * e.zigzag;

        if (e.y > canvas.height + e.size) {
          enemies.splice(i, 1);
          player.lives--;
          explode(e.x + e.size / 2, canvas.height - 20, '255,90,90');
          if (player.lives <= 0) gameOver = true;
          updateHud();
          continue;
        }

        const hitPlayer =
          Math.abs(e.x + e.size / 2 - player.x) < (e.size / 2 + player.width / 2 - 2) &&
          Math.abs(e.y + e.size / 2 - player.y) < (e.size / 2 + player.height / 2 - 2);

        if (hitPlayer) {
          enemies.splice(i, 1);
          explode(player.x, player.y, '255,130,130');
          player.lives--;
          if (player.lives <= 0) gameOver = true;
          updateHud();
          continue;
        }

        for (let j = bullets.length - 1; j >= 0; j--) {
          const b = bullets[j];
          if (b.x > e.x && b.x < e.x + e.size && b.y > e.y && b.y < e.y + e.size) {
            bullets.splice(j, 1);
            enemies.splice(i, 1);
            explode(e.x + e.size / 2, e.y + e.size / 2, '255,180,110');
            score += 10;
            defeated += 1;
            const nextLevel = Math.floor(defeated / 12) + 1;
            if (nextLevel !== level) level = nextLevel;
            updateHud();
            break;
          }
        }
      }
    }

    function draw() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      drawStars();

      drawPlayer();

      ctx.fillStyle = '#b6d6ff';
      for (const b of bullets) {
        ctx.beginPath();
        ctx.arc(b.x, b.y, b.r, 0, Math.PI * 2);
        ctx.fill();
      }

      enemies.forEach(drawEnemy);
      drawParticles();

      if (gameOver) {
        ctx.fillStyle = 'rgba(5, 9, 28, 0.75)';
        ctx.fillRect(0, 0, canvas.width, canvas.height);

        ctx.fillStyle = '#ffffff';
        ctx.textAlign = 'center';
        ctx.font = 'bold 52px Arial';
        ctx.fillText('GAME OVER', canvas.width / 2, canvas.height / 2 - 25);

        ctx.font = '24px Arial';
        ctx.fillStyle = '#c8d8ff';
        ctx.fillText(`Final Score: ${score}`, canvas.width / 2, canvas.height / 2 + 20);

        ctx.font = '18px Arial';
        ctx.fillStyle = '#8ec7ff';
        ctx.fillText('Press Enter to play again', canvas.width / 2, canvas.height / 2 + 58);
      }
    }

    function loop() {
      update();
      draw();
      if (!gameOver) requestAnimationFrame(loop);
    }

    document.addEventListener('keydown', (e) => {
      if (e.code === 'ArrowLeft' || e.code === 'ArrowRight' || e.code === 'Space') {
        keys[e.code] = true;
        e.preventDefault();
      }
      if (gameOver && e.code === 'Enter') resetGame();
    });

    document.addEventListener('keyup', (e) => {
      if (e.code === 'ArrowLeft' || e.code === 'ArrowRight' || e.code === 'Space') {
        keys[e.code] = false;
        e.preventDefault();
      }
    });

    updateHud();
    requestAnimationFrame(loop);
  </script>
</body>
</html>
""",
    height=610,
)
