var level = 1;
var levelupPoint = level * 30;
var tasksCompleted = 1;
document.getElementById("level").innerHTML = "score: " + score;

function myScore() {
  console.log("your score is : " + score);
  return score;
}
myScore();
