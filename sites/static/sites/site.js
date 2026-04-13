function hide(id,btn) {
    var elements = document.getElementsByClassName("InfoPanel");
    var buttons = document.getElementsByTagName("button");
    var page = document.getElementById(id);
    for (button of buttons) {
        button.style.background = "#d6d4c7";
    }
    btn.style.background = "#f5f3e6";
    for (element of elements) {
        console.log(element);
        element.style.display = "none";
    }
    page.style.display = "block";
    return
}

hide("StatementOfSignificance",document.getElementsByTagName("button")[0])
