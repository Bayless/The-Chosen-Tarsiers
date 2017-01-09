
// page colors in object used as dictionary
defaultColors={
    "background":"#FEFEFE",
    "header-text":"#000000",
    "paragraph-text":"#191919",
    "button":"#14679E",
    "top-bar":"#E6E6E6"
};

currentColors={
    "body":"#FEFEFE",
    "header-text":"#000000",
    "paragraph-text":"#191919",
    "button":"#14679E",
    "top-bar":"#E6E6E6"
};

//color changing functions

//change body
var getBodyColor = function(){
    console.log("body color: " + document.body.style.backgroundColor);
};


var changeBodyColor = function(color){
    document.body.style.backgroundColor = color;
    currentColors["body"] = color;
    console.log("body color: " + document.body.style.backgroundColor);
};

