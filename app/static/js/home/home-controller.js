angular.module('Flask mailer')
  .controller('HomeController', ['$scope', 'wiki', function ($scope, wiki) {
        $scope.status = "new";
        $scope.fullInfo = [];
        $scope.spamSentences = [];
        $scope.generateSpam = function(){
            if($scope.status != "pending"){
                $scope.status = "pending";
                wiki.getSpamSentences(5, function(wikiInfo){
                    $scope.status = "done";
                    $scope.fullInfo = wikiInfo;
                    $scope.spamSentences = _.pluck(wikiInfo.results, "random_sentence");
                });
            }
        }
  }]);
