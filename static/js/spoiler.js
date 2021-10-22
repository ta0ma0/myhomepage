function Spoiler() {
    var ele = document.getElementById("contentSpoiler");
    var text = document.getElementById("linkSpoiler");
    var table_tag = document.getElementById("top_after_spoiler")
    if (ele.style.display == "block") {
        ele.style.display = "none";
        text.innerHTML = "https://ruslanakmanov.link/expirience";
        table_tag.style.textAlign = "left"
        table_tag.style.verticalAlign = "middle"
    } else {
        ele.style.display = "block";
        text.innerHTML = "Hide &#172\;";
        table_tag.style.textAlign = "left";
        table_tag.style.verticalAlign = "top";
    }
}