

$(document).ready(function () {
  $(".owl-carousel .item").addClass("text-dark");

  $(".owl-carousel").owlCarousel({
    loop: true,
    margin: 20,

    responsiveClass: true,

    responsive: {
      0: {
        items: 1,
        nav: true,
        autoplay: true,
      },

      300: {
        items: 2,
        nav: true,
        autoplay: true,
      },

      400: {
        items: 3,
        nav: true,
        autoplay: true,
      },

      575: {
        items: 4,
        nav: true,
        autoplay: true,
      },

      800: {
        items: 5,
        nav: true,
        autoplay: true,
      },

      1500: {
        items: 6,
        nav: true,
        autoplay: true,
      },
    },
  });

  $(".plus-cart").click(function () {
    var id = $(this).attr("pid").toString();
    var ele=this.parentNode.children[2]
 
    $.ajax({
      type: "GET",
      url: "/pluscart",
      data: {
        prod_id: id
      },
      success: function (data) {
        ele.innerText= data.quantity


        document.getElementById("amount").innerText=data.amount
        document.getElementById("total").innerText=data.total

        document.getElementById("element").innerText=data.element

        document.getElementById("ship").innerText=data.shipping


        // $(".element").innerText(data.element)

        // document.getElementById("element").innerText = data.element



      },
    });
  });

  $(".minus-cart").click(function () {
    var id = $(this).attr("pid").toString();
    var ele=this
   
    $.ajax({
      type: "GET",
      url: "/minuscart",
      data: {
        prod_id: id
      },
      success: function (data) {
        
        

        if (data.quantity==0){
          ele.parentNode.parentNode.parentNode.parentNode.remove()
          // document.getElementById("current").remove()
        }
        else 
         {
          ele.parentNode.children[2].innerText=data.quantity
          // ele.innerText= data.quantity
         }

        document.getElementById("amount").innerText=data.amount
        document.getElementById("total").innerText=data.total


        document.getElementById("ship").innerText=data.shipping
        
        document.getElementById("element").innerText = data.element


        if(data.element == 0)
          {
            document.getElementById("place").remove()
          }


      },
    });
  });

  $(".remove-cart").click(function () {
    var id = $(this).attr("pid").toString();
    var ele=this
   
    $.ajax({
      type: "GET",
      url: "/removecart",
      data: {
        prod_id: id
      },
      success: function (data) {
        

   ele.parentNode.parentNode.parentNode.parentNode.remove()

   document.getElementById("element").innerText = data.element

        document.getElementById("amount").innerText=data.amount
        document.getElementById("total").innerText=data.total

        document.getElementById("ship").innerText=data.shipping


        // document.getElementById("current").remove()

        if(data.element == 0)
          {
            document.getElementById("place").remove()
          }
   
      },
    });
  });

});
