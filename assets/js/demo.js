import { cube, foo, graph } from './my-module.js';

siteData.setgraph = function  () {
    graph.options = {
        color:'blue',
        thickness:'3px'
    };
    graph.draw();
    console.log(cube(3));
    console.log(foo); 
};
