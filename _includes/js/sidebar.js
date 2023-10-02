function Drop() {

    var x = document.getElementById("section-links");
    if (x.style.display === "block") {
        x.style.display = "none";
        $("#myNavbar i")[0].className = "fa fa-bars"
    } else {
        x.style.display = "block";
        $("#myNavbar i")[0].className = "fa fa-close"
    }
    
};
  
window.onclick = function ( e ) {

    var atop = $("#myNavbar i")[0];
    var itop = $("#myNavbar .topnav")[0];
    var divtop = $("#myNavbar .w3-bar")[0];
    var navtop = $("#section-links")[0];
    
    if ( 
            navtop.style.display == "block" & e.target != divtop & e.target != atop & e.target != itop
    ) {
            navtop.style.display = "none";
            atop.className = "fa fa-bars";
      };

};