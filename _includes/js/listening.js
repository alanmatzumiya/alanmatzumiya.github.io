function Process ( func, data ) {

    function Resolve () {
        return new Promise(
        result => {
            setTimeout( () => { result( func(data) ) }, 1e3 )
        }
        );
    };

    async function Exec () {
        const result = await Resolve();
        console.log(result);
    };

    return Exec;

};

class ServerDispatcher {

    constructor () {

        this.host = "192.168.50.16";
        this.port = "5050";
        this.url = "http://192.168.50.16:5050";
    }    

    getdata ( args ) {      
        var path = args.path;
        var data = args.data;
        var urldata = this.url;
        if ( typeof path != "undefined" ) {
            if ( path.startsWith( "/" ) ) {
                urldata += path;                
            } else {
                urldata += "/" + path;
            };            
        };
        $.getJSON(
            urldata, data,
            ( res ) => setTimeout(
                () => print( res ), 5e2
            )
        );
    };     

    postdata ( args ) {
        var path = args.path;
        var data = args.data;
        var urldata = [ this.url, path ].join(
            ( path.startsWith( "/" ) ) ? "" : "/"
        );        
        $.post(
            urldata, data,
            ( res ) => setTimeout( 
                () => print( res ), 5e2 
            )
        );
    }

}


var siteData = {{ site.data | jsonify }};