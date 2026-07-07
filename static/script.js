let total = 0;
let normal = 0;
let attack = 0;

function simulateTraffic() {
    total++;
    normal++;

    document.getElementById("total").innerHTML = total;
    document.getElementById("normal").innerHTML = normal;
    document.getElementById("status").innerHTML = "Normal Traffic";
}

function simulateAttack() {
    total += 50;
    attack += 50;

    document.getElementById("total").innerHTML = total;
    document.getElementById("attack").innerHTML = attack;
    document.getElementById("status").innerHTML = "⚠️ DDoS Attack Detected";
}