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

// Slugify supplied text
function slugify(text){
    text = text.toLowerCase();
    text = text.replace(" ", "-");
    return text;
}

// If there is a hash in the url, slugify it
// and replace
if(window.location.hash) {
    // Fragment exists
    slug = slugify(window.location.hash);
    history.replaceState(undefined, undefined, slug)
    //window.location.hash = slug;
    document.location.replace(window.location.href);
}
