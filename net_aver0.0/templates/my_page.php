<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="sanitize" type="text/css" href="sanitize.css">
    <link rel="stylesheet" type="text/css" href="style.css">
    <title>Document</title>
</head>
<body>
<header>
        <?php 
            include'header.php';
            //echo "$header"; 
        ?>
</header>
<main class="body_color">
    <div class="mp_title">
        <h2>こんにちは、熱田さん</h2>
    </div>
    <section class="my_menu">
        <a href="setting.php">ステータス</a>
        <a href="index.php">ホーム</a>
        <a href="my_like.php">お気に入り</a>
        <a href="add_fish.php">記事を投稿</a>
        <a href="">自分の魚</a>
        <a href="index.php">ログアウト</a>
        <!--<div>閲覧履歴</div>-->
    </section>
</main>

<footer>
    <?php 
        include'footer.php';
    ?>
</footer>
</body>
</html>
