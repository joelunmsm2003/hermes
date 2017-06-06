
function Cotiza($scope,$http,$filter,$location,$localStorage) {

    $scope.riesgo = 8

    $scope.categoria = 1

    $scope.ubicL= true

    $scope.ubicP= true


      function urlBase64Decode(str) {
        var output = str.replace('-', '+').replace('_', '/');
        switch (output.length % 4) {
            case 0:
                break;
            case 2:
                output += '==';
                break;
            case 3:
                output += '=';
                break;
            default:
                throw 'Illegal base64url string!';
        }
        return window.atob(output);
    }


    function getUserFromToken() {
        var token = $localStorage.token;
        var user = {};
        if (typeof token !== 'undefined') {
            var encoded = token.split('.')[1];
            user = JSON.parse(urlBase64Decode(encoded));
        }
        return user;
    }

    console.log('User',getUserFromToken().user_id)

    $scope.user = getUserFromToken().user_id

    








    $scope.antiguedad = [{
    id: 1,
    label: 'Nuevo',
   
    }, {
    id: 2,
    label: 'Usado',
  
    }];

    $scope.est_antiguedad = 'False'

    $scope.model = {}

    console.log($scope.antiguedad)

    $scope.data = function (todo) {

        console.log('hdhdhd',todo)


    }

    $scope.antig = function (todo) {

        console.log(todo)

        if($scope.model.modelo.id_modelo == undefined){


            console.log('ksksksk')
        }



        id_modelo = $scope.model.modelo.id_modelo



        if(todo.antiguedad.label == 'Usado'){

            $http.get(host+"/precio/"+id_modelo+'/'+todo.anio.anio_antig).success(function(response) {

            console.log('precio',response)

           

            $http.get(host+"/preciodreprecio/"+response).success(function(response) {

            $scope.precio = response

            });

            });



          
        }

        if(todo.antiguedad.label == 'Nuevo'){

            //$scope.CurrentDate = new Date()

            //anio = $filter('date')($scope.CurrentDate, 'yyyy')

            
            $http.get(host+"/precio/"+id_modelo+'/'+todo.anio.anio_antig).success(function(response) {

            console.log('precio',response)

            $scope.precio = response

            });






        }

    }


    $scope.logear = function (todo) {

        console.log

       
        $http({
        url: host+"/logearse/",
        data: todo,
        method: 'POST',
     
        }).
        success(function(data) {
          
          console.log(data)

        })

    }

    $http.get(host+"/estadologin/").success(function(response) {$scope.estadologin = response;

      
    });


    $http.get(host+"/marca/").success(function(response) {$scope.marca = response;

      
    });

    $http.get(host+"/uso/").success(function(response) {$scope.uso = response;

      
    });

    $http.get(host+"/anio/").success(function(response) {$scope.anio = response;


        console.log($scope.anio[12])
        $scope.model.anio = $scope.anio[0]

      
    });


    $http.get(host+"/timon/").success(function(response) {$scope.timon = response;

      
    });

    $http.get(host+"/modalidad/").success(function(response) {$scope.modalidad = response;

      
    });

    //console.log($scope.items);




    $scope.obtenermodelo = function (data) {

       
    $http.get(host+"/modelo/"+data.marca.id_marca+'/').success(function(response) {

        $scope.modelo = response

        console.log($scope.modelo)

      
    });

    }

    


       
    $scope.obtenerclase = function (data) {
    
        $http.get(host+"/claseModelo/"+data.modelo.id_modelo+'/').success(function(response) {

            $scope.claseModelo = response

            console.log('claseModelo',response)

            $scope.vari= $scope.claseModelo[0].id

            $http.get(host+"/riesgomodelo/"+$scope.vari+'/').success(function(response) {

            console.log("/riesgomodelo/",response)

            varx = ''

            for (var i = 0; i < response.length; i++) {

                varx = varx +response[i].aseguradora__name_asegurad+'aseg'+response[i].id_riesg_id+'riesg'
            }

      


            $scope.riesgo = varx

            if (varx==''){

                $scope.riesgo = 3
            }



           
        });

       

      
    });





    }

    $scope.programa = 3

    $scope.ubicacion = 1


    $scope.obtenerprecio = function (data) {

        console.log('obtenerprecio',data)

  

        $http.get(host+"/precio/"+$scope.model.claseModelo.id_modelo+'/'+data.anio.anio_antig+'/').success(function(response) {

        console.log('precio',response)

        $scope.precio = response
             
        });





    }


$scope.items = [{
id: 1,
label: 'Lima'
}, {
id: 2,
label: 'Provincia'
}];

$scope.selected = $scope.items[0];





        $scope.saveContact = function (model,precio,check,ubicP,ubicL) {





       console.log('SAVE',model)

       modelo = model.modelo.id_modelo


        var todo={

            add: "Guardar",
            dato: model,
            precio:precio,
            ubicL:ubicL,
            ubicP:ubicP,
            check:check,
            modelo:modelo,
            done:false
        }



        if ($scope.check== 1){

            $scope.model.statuscheck = 1
        }
        else{
            $scope.model.statuscheck = 0

        }

        console.log('check',$scope.model.check)
        

        if ($scope.ubicL== 1){

            $scope.model.statusubicL = 1
        }
        else{
            $scope.model.statusubicL = 0

        }        

        console.log('ubicL',$scope.model.ubicL)

        if ($scope.ubicP== 1){

            $scope.model.statusubicP = 1
        }
        else{
            $scope.model.statusubicP = 0

        }  
        
        console.log('ubicP',$scope.model.ubicP)

        $http({
        url: host+"/cotiSave/",
        data: todo,
        method: 'POST',
     
        }).
        success(function(data) {


        $location.url('/resultado/'+data+'/'+model.uso.id_uso+'/'+model.anio.id_anio+'/'+model.modalidad.id_modalidad+'/4z2z25z/'+model.modelo.id_modelo+'/'+$scope.precio)
       

        })


        
    };


}

