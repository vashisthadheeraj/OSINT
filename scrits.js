const buttons = document.querySelectorAll('.osint-btn');
const hackSound = document.getElementById('hack-sound');

buttons.forEach(button => {
  button.addEventListener('click', () => {
    playHackSound();
  });
});

function playHackSound() {
  hackSound.currentTime = 0;
  hackSound.play();
}
