var instances;
  
  document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('select');
    instances = M.FormSelect.init(elems);
    document.body.addEventListener('change', function(e){
        // console.log(instances);
        instances.forEach((instance, index) => {
            setTimeout(function(){ 
                console.log(index,  instance.getSelectedValues())
            }, 100);
        });
      })
  });

