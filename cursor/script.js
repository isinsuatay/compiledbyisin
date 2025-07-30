const button = document.getElementById('escapeBtn');
const container = document.querySelector('.container');

container.addEventListener('mousemove', (e) => {
  const btnRect = button.getBoundingClientRect();
  const btnX = btnRect.left + btnRect.width / 2;
  const btnY = btnRect.top + btnRect.height / 2;
  const distance = Math.hypot(e.clientX - btnX, e.clientY - btnY);

  if (distance < 100) { // Fare 100px yaklaştığında
    moveButton();
  }
});

function moveButton() {
  const containerWidth = window.innerWidth - button.offsetWidth;
  const containerHeight = window.innerHeight - button.offsetHeight;

  const randomX = Math.floor(Math.random() * containerWidth);
  const randomY = Math.floor(Math.random() * containerHeight);

  button.style.left = `${randomX}px`;
  button.style.top = `${randomY}px`;

  // Zıplama efekti 
  button.classList.add('jump');
  setTimeout(() => button.classList.remove('jump'), 300);
}