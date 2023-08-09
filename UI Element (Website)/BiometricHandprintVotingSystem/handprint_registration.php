<!DOCTYPE html>
<html>
<head>
    <title>Login using Handprints - Biometric Handprint Voting System</title>
    <link rel="stylesheet" href="assets/css/bootstrap.min.css">
    <link rel="stylesheet" href="assets/css/style.css">
    <style>
        body {
            background-color: black;
            margin: 0;
            padding: 0;
        }
        
        .container {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        
        .handprint_image {
            width: 100%;
            height: 100%;
            object-fit: contain;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="d-flex justify-content-center">
            <div class="user_card">
                <div class="d-flex justify-content-center mt-3">
                    <img src="assets/images/ScanPrompt.png" class="handprint_image" alt="Handprint Image">
                </div>

                <div class="d-flex justify-content-center mt-3">
                    <form method="POST">
                        <!-- ... form fields for handprint registration ... -->
                    </form>   
                </div>

                <div class="mt-4">
                    <div class="d-flex justify-content-center links">
                        <a href="index.php?sign-up=1" class="text-white">Continue to Sign Up</a>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <script src="assets/js/jquery.min.js"></script>
    <script src="assets/js/bootstrap.min.js"></script>

</body>
</html>
