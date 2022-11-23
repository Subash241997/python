<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />
    <meta http-equiv="x-ua-compatible" content="ie=edge" />
    <title>Url-Copy</title>
    <!-- MDB icon -->
    <link rel="icon" href="img/mdb-favicon.ico" type="image/x-icon" />
    <!-- Font Awesome -->
    <link
      rel="stylesheet"
      href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css"
    />
    <!-- Google Fonts Roboto -->
    <link
      rel="stylesheet"
      href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700;900&display=swap"
    />
    <!-- MDB -->
    <link rel="stylesheet" href="css/mdb.min.css" />
  </head>
  <body>
    <!-- Start your project here-->

    <h4>

    <?php
        // Check if the "mobile" word exists in User-Agent
        $isMob = is_numeric(strpos(strtolower($_SERVER["HTTP_USER_AGENT"]), "mobile"));

        // Check if the "tablet" word exists in User-Agent
        $isTab = is_numeric(strpos(strtolower($_SERVER["HTTP_USER_AGENT"]), "tablet"));

        // Platform check
        $isWin = is_numeric(strpos(strtolower($_SERVER["HTTP_USER_AGENT"]), "windows"));
        $isAndroid = is_numeric(strpos(strtolower($_SERVER["HTTP_USER_AGENT"]), "android"));
        $isIPhone = is_numeric(strpos(strtolower($_SERVER["HTTP_USER_AGENT"]), "iphone"));
        $isIPad = is_numeric(strpos(strtolower($_SERVER["HTTP_USER_AGENT"]), "ipad"));
        $isIOS = $isIPhone || $isIPad;


        if($isIOS){
        echo 'iOS';
        }elseif($isAndroid){
        echo 'ANDROID';
        }elseif($isWin){
        echo 'WINDOWS';
        }

        ?></h4>
        <div class="d-flex justify-content-center flex-column" style="position: fixed; z-index: 1000; height: 70vh">

        <!-- Whatsapp -->
        <a class="btn text-white mb-1" style="background-color: #25d366;" href="#!" role="button" onclick="whatsapp('<?php echo $_SERVER['HTTP_HOST'].$_SERVER['REQUEST_URI']; ?>');">
        <i class="fab fa-whatsapp"></i>
        </a>

            <!-- messanger -->
            <a class="btn text-white mb-1" style="background: linear-gradient(0deg, rgba(14,2,222,1) 0%, rgba(237,0,255,1) 100%);   " href="#!" role="button" onclick="messanger('<?php echo $_SERVER['HTTP_HOST'].$_SERVER['REQUEST_URI']; ?>');">
                <i class="fas fa-comment"></i>
            </a>
  
        <!-- Twitter -->
        <a class="btn text-white mb-1" style="background-color: #55acee;" href="#!" role="button" onclick="twitter('<?php echo $_SERVER['HTTP_HOST'].$_SERVER['REQUEST_URI']; ?>');">
        <i class="fab fa-twitter"></i>
        </a>
  
        <!-- Google -->
        <a class="btn text-white mb-1" style="background-color: #dd4b39;" href="#!" role="button" onclick="gmail('<?php echo $_SERVER['HTTP_HOST'].$_SERVER['REQUEST_URI']; ?>');">
        <i class="fab fa-google"></i>
        </a>

        <!-- SMS -->
        <a class="btn text-white mb-1" style="background-color: #4c75a3;" href="#!" role="button" onclick="sms('<?php echo $_SERVER['HTTP_HOST'].$_SERVER['REQUEST_URI']; ?>', <?php echo $isIOS ?>);">
        <i class="fas fa-sms"></i>
        </a>
  
        <!-- copy -->
        <a class="btn text-white mb-1" style="background-color: #ac2bac;" href="#!" role="button" onclick="copy('<?php echo $_SERVER['HTTP_HOST'].$_SERVER['REQUEST_URI']; ?>')">
        <i class="fas fa-copy"></i>
        </a>

        </div>
    <!-- End your project here-->

    <!-- MDB -->
    <script type="text/javascript" src="/js/mdb.min.js"></script>
    <!-- Custom scripts -->
    <script type="text/javascript">

        function whatsapp(text){
            var cop = 'https://'+text;
            var whatsapp = 'https://api.whatsapp.com/send/?phone=&text=I+found+this+blog+Interesting.+You+can+read+it+here:%0A%0A+'+ cop;
            window.open(whatsapp);
        }

        function messanger(text){
            var cop = 'https://'+text;
            //var messanger = 'https://www.messenger.com/t/search/?messages='+cop;
            //var messanger = 'https://www.messenger.com/t/?select=&text='+cop;
            //var messanger = 'https://www.linkedin.com/sharing/share-offsite/?url='+cop;
            window.open(cop);
        }

        function twitter(text){
            var cop = 'https://'+text;
            var twitter = 'https://twitter.com/intent/tweet?text=I+found+this+blog+Interesting.+You+can+read+it+here:%0A%0A+'+cop;
            window.open(twitter);
        }

        function gmail(text){
            var cop = 'https://'+text;
            var gmail = "mailto:?Subject=Hello,%20I%20found%20this%20interesting.&Body=I%20found%20this%20blog%20interesting.%20You%20can%20read%20it%20here.%0A%0A"+cop;
            window.open(gmail);
        }

        function sms(text, platform){
            var cop = 'https://'+text;
            if(platform=="iOS"){
                var sms = 'sms:&body=I found this blog Interesting. You can read  it  here:%0A%0A+'+cop;
            }
            else{
                var sms = 'sms:?body=I+found+this+blog+Interesting.+You+can+read+it+here:%0A%0A+'+cop;
            }

            window.open(sms);
        }

        function copy(text){
            var cop = 'https://'+text;
            alert("Hello! This website URL is copied.");
            copyToClipboard(cop);
        }
    </script>
  </body>
</html>
