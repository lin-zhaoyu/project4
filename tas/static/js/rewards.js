var level = 1;
var levelupPoint = level * 30;
var tasksCompleted = 1;
document.getElementById("level").innerHTML =
  "do 5 more tasks to unlock more animations!: " + score;

function myScore() {
  console.log("your score is : " + score);
  return score;
}
if (score == 5) {
  console.log("you socre are five");
}
const canvas = document.getElementById("canvas1");
myScore();

const ctx = canvas.getContext("2d");
const CANVAS_WIDTH = (canvas.width = 600);
const CANVAS_HEIGHT = (canvas.height = 600);
const playerImage = new Image();
playerImage.src = "../../static/images/shadow_dog.png";
const spriteWidth = 575;
const spriteHeight = 523;
let frameX = 0;
let frameY = 0;
let gameFrame = 0;
const staggerFrames = 5;
console.log("hi!");
function animate() {
  console.log("animating!");
  ctx.clearRect(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT);
  //ctx.fillRect (100, 50, 100, 100);
  //ctx.drawImage (image, sx, sy, sw, sh, dx, dy, dw, dh);
  ctx.drawImage(
    playerImage,
    frameX * spriteWidth,
    frameY * spriteHeight,
    spriteWidth,
    spriteHeight,
    0,
    0,
    spriteWidth,
    spriteHeight
  );
  //   ctx.drawImage(playerImage, 0, 0);
  if (gameFrame % staggerFrames == 0) {
    if (frameX < 6) frameX++;
    else frameX = 0;
  }
  gameFrame++;
  requestAnimationFrame(animate);
}
animate();
