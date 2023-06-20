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

        this.host = "192.168.50.216";
        this.port = "5050";
        this.url = "http://192.168.50.216:5050";
    }    

    get ( path="/", data={} ) {
        $.getJSON(
            this.url+"/api/get"+path, data,
            ( res ) => setTimeout(
                () => print( res ), 5e2
            )
        );
    }
        
    post ( path="/", data={} ) { 
        $.post(
            this.url+"/api/post"+path, data,
            ( res ) => setTimeout( 
                () => print( res ), 5e2
            )
        );
    }

}
