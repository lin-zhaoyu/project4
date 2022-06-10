var level = 1;
var levelupPoint = level * 30;
var tasksCompleted = 1;
document.getElementById("level").innerHTML =
  "Do tasks to unlock more animations!";

function myScore() {
  console.log("your score is : " + score);
  return score;
}
if (score == 5) {
  console.log("you score is five");
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
let frameY = -1;
let limit = -1;
let staggerFrames = -1;
let gameFrame = 0;

const dogState = [
  {
    name: "idle",
    frameY: 0,
    limit: 6,
    staggerFrames: 7,
  },
  {
    name: "run",
    frameY: 3,
    limit: 6,
    staggerFrames: 7,
  },
  {
    name: "dazed",
    frameY: 4,
    limit: 10,
    staggerFrames: 7,
  },
  {
    name: "roll",
    frameY: 6,
    limit: 6,
    staggerFrames: 7,
  },
  {
    name: "bite",
    frameY: 7,
    limit: 6,
    staggerFrames: 7,
  },
  {
    name: "derp",
    frameY: 8,
    limit: 11,
    staggerFrames: 10,
  },
  {
    name: "stanky-leg",
    frameY: 9,
    limit: 3,
    staggerFrames: 10,
  },
];

function playAnimation(number) {
  frameY = dogState[number].frameY;
  limit = dogState[number].limit;
  staggerFrames = dogState[number].staggerFrames;
  return [frameY, limit, staggerFrames];
}
//animation = get stuff from drop down menu
animation = "stanky-leg";
if (animation == "idle") {
  playAnimation(0);
  //   console.log(setFrame(0));
}
if (animation == "run") {
  playAnimation(1);
}
if (animation == "dazed") {
  playAnimation(2);
}
if (animation == "roll") {
  playAnimation(3);
}
if (animation == "bite") {
  playAnimation(4);
}
if (animation == "derp") {
  playAnimation(5);
}
if (animation == "stanky-leg") {
  playAnimation(6);
}

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
    if (frameX < limit) frameX++;
    else frameX = 0;
  }
  gameFrame++;
  requestAnimationFrame(animate);
}
animate();
