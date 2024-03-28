<!DOCTYPE html>
<html lang="en">
<body>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="sanitize" type="text/css" href="sanitize.css">
    <!--スライドショーにslickを使う-->
    <link rel="stylesheet" href="./slick/slick.css"><link rel="stylesheet" href="./slick/slick-theme.css">
    <link rel="stylesheet" type="text/css" href="style.css">
    <title>NetA</title>
</head>
<header>
    <?php include'header.php';//echo "$header"; ?>
</header>
<main id="setting">
<section>
    <h2>飼っている魚・近くの魚を投稿</h2>
    <table>
        <tbody>
        <tr class="form_table">
            <th>性別</th>
            <td>
                選択なし<input type="radio" name="sex" value="0">
                オス<input type="radio" name="sex" value="1">
                メス<input type="radio" name="sex" value="2">
            </td>
        </tr>
        </tbody>
        <tbody>
        <tr class="form_table">
            <th>備考</th>
            <td><input type="text"></td>
        </tr>
        </tbody>
        <tbody>
        <tr class="form_table">
        <th>飼育平均温度</th>
            <td>
                <select name="temp_value">
                    <option>選択なし</option>
                    <option>~20</option>
                    <option>20~25</option>
                    <option>25</option>
                    <option>26</option>
                    <option>27</option>
                    <option>28</option>
                    <option>29</option>
                    <option>30~</option>
                </select> 度
            </td>
        </tr>
        </tbody>
        <tbody>
        <tr class="form_table">
            <th>飼育水槽サイズ</th>
            <td>
                <select name="tank_value">
                    <option>選択なし</option>
                    <option>~25</option>
                    <option>30</option>
                    <option>45</option>
                    <option>60</option>
                    <option>90</option>
                    <option>100</option>
                    <option>120</option>
                    <option>150</option>
                    <option>180</option>
                    <option>180~</option>
                </select> cm
            </td>
        </tr>
        </tbody>
        
        <tbody>
        <tr class="form_table">
            <th>飼育に使っている用品</th>
            <td><input type="text"></td>
        </tr>
        </tbody>
        
        <tbody>
        <tr class="form_table">
            <th>大きさ</th>
            <td><input type="number"> cm</td>
        </tr>
        </tbody>
        <tbody>
        <tr class="form_table">
            <th>餌</th>
            <td>
                人工飼料（粒）<input name="hood_value" type="checkbox">
                人工飼料（フレーク）<input name="hood_value" type="checkbox">
                クリル<input name="hood_value" type="checkbox">
                赤虫<input name="hood_value" type="checkbox">
                その他冷凍生餌<input name="hood_value" type="checkbox">
                ミルワーム<input name="hood_value" type="checkbox">
                コオロギ<input name="hood_value" type="checkbox">
                その他虫<input name="hood_value" type="checkbox">
                どじょう<input name="hood_value" type="checkbox">
                金魚<input name="hood_value" type="checkbox">
                キビナゴ<input name="hood_value" type="checkbox">
                エビ<input name="hood_value" type="checkbox">
                その他魚<input name="hood_value" type="checkbox">
                
                その他<input type="text">

            
            </td>
        </tr>
        </tbody>
        <tbody>
        <tr class="form_table">
            <th>生息地</th>
            <td><input type="text"></td>
        </tr>
        </tbody>
        <tbody>
        <tr class="form_table">
            <th>分類</th>
            <td><input type="text"></td>
        </tr>
        </tbody>
    </table>
    <input class="button" type="submit" value="確認画面へ">
</section>    
</main>

<footer>
    <?php 
        include'footer.php';
    ?>
</footer>
</body>
</html>