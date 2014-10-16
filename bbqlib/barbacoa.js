window.$_BBQ = {
    sw: 1,
    request: function(action, params, callback){
        if (!params) params = [];
        this.callback = callback;
        window.location = '#BBQ' + this.sw + '::' + action + '|' + JSON.encode(params);
        this.sw = (this.sw == 1 ? 2 : 1);
    },

    execute_callback: function(content){
        this.callback(content);
    }
};

window.Barbacoa = {

    version: 0.1,

    File: {
        write: function(filename, content) {
            $_BBQ.request('File.write', [filename, content]);
        }
    },

    Environment: {
        get_user_home: function(callback){
            $_BBQ.request('Environment.get_user_home', [], callback);
        }

    }

};

if (typeof(BarbacoaReady) == 'function'){
    BarbacoaReady();
}