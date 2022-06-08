var level = 1;
var levelupPoint = level * 30;
var tasksCompleted = 1;

document.getElementById("level").innerHTML = "level: " + level;

document.getElementById("progress").innerHTML = "progress: " + tasksCompleted + " / " + levelupPoint;
