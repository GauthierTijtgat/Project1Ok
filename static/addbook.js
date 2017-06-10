/**
 * Created by Gaultier Tijtgat on 9/06/2017.
 */

$(function () {

    $('#submit').click(function () {


        $.ajax({
            url: '/addbook',
            data: $('form').serialize(),
            type: 'post',
            succes: function (response) {
                console.log(response);

            },
            error: function (error) {
                console.log(error)

            }


        });



    });


});