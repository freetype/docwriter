/*
Internal link topbar offest adjust Javascript
Code provided by @makshh on GitHub

Bug report on material-mkdocs
  https://github.com/squidfunk/mkdocs-material/issues/791
*/

// Offset top helper
function offsetY(elem) {
    if(!elem) elem = this;
    var y = elem.offsetTop;
    while (elem = elem.offsetParent) {
        y += elem.offsetTop;
    }
    return y;
}

var links = document.getElementsByTagName('a');
for(var i = 0; i < links.length; i++) {
    links[i].onclick = function (event) {
        var o = document.getElementById(this.hash.substr(1));
        if(this.href.indexOf(window.location.pathname) > -1) {
            event.preventDefault();
            var sT = offsetY(o) - document.getElementsByClassName('md-header')[0].clientHeight;
            window.location.hash = this.hash;
            window.scrollTo(0, sT);
            console.log(offsetY(o))
        }
    }
}