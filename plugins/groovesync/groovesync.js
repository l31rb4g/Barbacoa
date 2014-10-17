Barbacoa.Plugin.add({

    getUserData: function(username){
        var data = Barbacoa.Plugin.execute('GrooveSync', 'getUserData', [username]);
        alert(data);
    }

});