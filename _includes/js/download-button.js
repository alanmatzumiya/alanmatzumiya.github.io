document.addEventListener( "DOMContentLoaded", function () {
    this.querySelector( "#download-btn" ).addEventListener( "click", function () {
        let waitClass = "waiting", runClass = "running", cl = this.classList;
        if ( !cl.contains( waitClass ) && !cl.contains( runClass ) ) {
            cl.add(waitClass);
            setTimeout( function () {
                cl.remove( waitClass );
                setTimeout( function () {
                    cl.add( runClass );
                    setTimeout( function () {
                        cl.remove( runClass );
                        window.location.href = "{{ site.url }}/{{ author.cv-pdf }}";
                    }, 4e3 );
                }, 2e2 );
            }, 1.8e3 );
        };
    } );
} );