angular.module('Flask mailer')
    .factory('wiki', function($http){
        var endpoint = "/api/wiki_topic";
        return {
            getSpamSentences: function(sentences, cb){
                $http.get(endpoint + "?rows=" + sentences)
                    .success(cb)
                    .error(function(data){
                        console.error("There was an error processing the request");
                    });
            }
        };
    });