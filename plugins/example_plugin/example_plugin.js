new Barbacoa.Plugin({

    get_ip: function(){
        var my_ip = this.execute('ExamplePlugin', 'get_my_ip');
        alert('My IP is ' + my_ip);
    }

});