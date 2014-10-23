new Barbacoa.Plugin({

    get_python_version: function(){
        var version = this.execute('ExamplePlugin', 'get_version');
        return version;
    }

});