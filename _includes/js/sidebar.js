$( "#navbar-button" )[0].onclick = function () {
    var x = $( "#section-links" )[0];
    if ( x.style.display === "block" ) {
        hide( x );
        $( "#myNavbar i" )[0].className = "fa fa-bars"
    } else {
        show( x );
        $( "#myNavbar i" )[0].className = "fa fa-close"
    }
};
  
window.onclick = function ( e ) {
    var atop = $( "#myNavbar i" )[0],
        itop = $( "#myNavbar .topnav" )[0],
        divtop = $( "#myNavbar .w3-bar" )[0],
        navtop = $( "#section-links" )[0];
    if ( all([
            navtop.style.display == "block",
            e.target != divtop,
            e.target != atop,
            e.target != itop
    ]) ) {
            hide( navtop );
            atop.className = "fa fa-bars";
      };
};