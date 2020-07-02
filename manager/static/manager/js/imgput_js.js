  var elem = document.getElementById('range');
  var target = document.getElementById('value');
  var rangeValue = function (elem, target) {
    return function(evt){
      target.innerHTML = elem.value;
      context.lineWidth = elem.value;
    }
  }
  elem.addEventListener('input', rangeValue(elem, target));
//画像プレビュー
function previewImage(obj)
{
	var fileReader = new FileReader();
	fileReader.onload = (function() {
		document.getElementById('preview').src = fileReader.result;
	});
	fileReader.readAsDataURL(obj.files[0]);
}

//現在時刻
function ChangeParaToDate() {
document.getElementById('eid_date').innerHTML = Date();
}


// // canvas要素を取得
// var canvas = document.getElementById( "draw-area" ) ;
// // img要素を取得
var image = document.getElementById( "preview" ) ;
var text_areas = document.getElementById("message");
// キャンバスのデータをpngに変換する
function canvas_to_base64() {
    var canvas = document.getElementById("draw-area") ;
	var image_data = canvas.toDataURL("image/png");

  // 描画内容をデータURIに変換する (引数なしだとPNG)
	var dataURI = canvas.toDataURL() ;
	image.src = dataURI;

	// image_data = image_data.replace(/^.*,/, '');
	// var form = document.form;
	// form.imagedata.value = image_data;
	// form.submit();
    // POSTでアップロード

    count = 0;  //アニメーション
    start();    //アニメーション

    var fData = new FormData();
    fData.append('image', dataURI);
    csrfSetting();
            // ajax送信
        $.ajax({
          //画像処理サーバーに返す場合
            url: 'http://127.0.0.1:8000/manager/HandRecognize/',
            type: 'POST',
            data: fData,
            contentType: false,
            processData: false,
            success: function (data, dataType) {
                $("#string").text(data);
                //非同期で通信成功時に読み出される [200 OK 時]
                console.log('Success', data);
              },
            error: function (XMLHttpRequest, textStatus, errorThrown) {
                $("#string").text(errorThrown);
                //非同期で通信失敗時に読み出される
                console.log('Error : ' + errorThrown);

            }
        });

}
//アニメーション
  var INTERVAL = 30; // ms
  var canvas = document.getElementById('draw-area');
  var ctx = canvas.getContext('2d');

  function drawFrame() {
    // 半径 20px の円を中央に描く
      var x = Math.random() * canvas.width;
      var y = Math.random() * canvas.height;
      ctx.fillStyle = randomColor();  // 塗りつぶしの色
      ctx.fillRect(x, y, 50, 50);
  }

  function randomColor() {
      return '#' + Math.floor(Math.random() * 0xFFFFFF).toString(16);
  }
  var count = 0;
  function start() {
      var id = setTimeout(function() {
          drawFrame();
          start();
    }, INTERVAL);
    count++;
    if(count >-1){ clearTimeout(id);}
  }
//↑アニメーション

// 2 csrfを取得、設定する関数
function getCookie(key) {
    var cookies = document.cookie.split(';');
    for (var _i = 0, cookies_1 = cookies; _i < cookies_1.length; _i++) {
        var cookie = cookies_1[_i];
        var cookiesArray = cookie.split('=');
        if (cookiesArray[0].trim() == key.trim()) {
            return cookiesArray[1]; // (key[0],value[1])
        }
    }
    return '';
}
function csrfSetting() {
    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
            }
        }
    });
}

// 3 POST以外は受け付けないようにする関数
function csrfSafeMethod(method) {
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
//

// var request = {
//     url: 'http://localhost:4567/base64',
//     method: 'POST',
//     params: {
//         image: base64.replace(/^.*,/, '')
//     },
//     success: function (response) {
//         console.log(response.responseText);
//     }
// };
canvasClear()
//キャンバスの背景色を白にしている
//そのままだと無地になる
function canvasClear() {
    canvas = document.getElementById("draw-area");
    ctx = canvas.getContext("2d");
    ctx.fillStyle = "#FFFFFF";//筆に白い絵の具をつけて
    ctx.fillRect(0, 0, 420, 420);//四角を描く
}
//-----------------------------------------------
var context = canvas.getContext('2d');
context.lineWidth = 15;

// ページの読み込みが完了したらコールバック関数が呼ばれる
// ※コールバック: 第2引数の無名関数(=関数名が省略された関数)
window.addEventListener('load', () => {
  const canvas = document.querySelector('#draw-area');
  // contextを使ってcanvasに絵を書いていく
  // const context = canvas.getContext('2d');


  // 直前のマウスのcanvas上のx座標とy座標を記録する
  const lastPosition = { x: null, y: null };

  // マウスがドラッグされているか(クリックされたままか)判断するためのフラグ
  let isDrag = false;
  let currentColor = '#000000';
  // 絵を書く
  function draw(x, y) {
    // マウスがドラッグされていなかったら処理を中断する。
    // ドラッグしながらしか絵を書くことが出来ない。
    if(!isDrag) {
      return;
    }

    // 「context.beginPath()」と「context.closePath()」を都度draw関数内で実行するよりも、
    // 線の描き始め(dragStart関数)と線の描き終わり(dragEnd)で1回ずつ読んだほうがより綺麗に線画書ける

    // 線の状態を定義する
    // MDN CanvasRenderingContext2D: https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D/lineJoin
    context.lineCap = 'round'; // 丸みを帯びた線にする
    context.lineJoin = 'round'; // 丸みを帯びた線にする
    // context.lineWidth = 20; // 線の太さ
    context.strokeStyle = currentColor; // 線の色

    // 書き始めは lastPosition.x, lastPosition.y の値はnullとなっているため、
    // クリックしたところを開始点としている。
    // この関数(draw関数内)の最後の2行で lastPosition.xとlastPosition.yに
    // 現在のx, y座標を記録することで、次にマウスを動かした時に、
    // 前回の位置から現在のマウスの位置まで線を引くようになる。
    if (lastPosition.x === null || lastPosition.y === null) {
      // ドラッグ開始時の線の開始位置
      context.moveTo(x, y);
    } else {
      // ドラッグ中の線の開始位置
      context.moveTo(lastPosition.x, lastPosition.y);
    }
    // context.moveToで設定した位置から、context.lineToで設定した位置までの線を引く。
    // - 開始時はmoveToとlineToの値が同じであるためただの点となる。
    // - ドラッグ中はlastPosition変数で前回のマウス位置を記録しているため、
    //   前回の位置から現在の位置までの線(点のつながり)となる
    context.lineTo(x, y);

    // context.moveTo, context.lineToの値を元に実際に線を引く
    context.stroke();

    // 現在のマウス位置を記録して、次回線を書くときの開始点に使う
    lastPosition.x = x;
    lastPosition.y = y;
  }

  // canvas上に書いた絵を全部消す
  function clear() {
    context.clearRect(0, 0, canvas.width, canvas.height);
    canvasClear()
  }

  // マウスのドラッグを開始したらisDragのフラグをtrueにしてdraw関数内で
  // お絵かき処理が途中で止まらないようにする
  function dragStart(event) {
    // これから新しい線を書き始めることを宣言する
    // 一連の線を書く処理が終了したらdragEnd関数内のclosePathで終了を宣言する
    context.beginPath();

    isDrag = true;
  }
  // マウスのドラッグが終了したら、もしくはマウスがcanvas外に移動したら
  // isDragのフラグをfalseにしてdraw関数内でお絵かき処理が中断されるようにする
  function dragEnd(event) {
    // 線を書く処理の終了を宣言する
    context.closePath();
    isDrag = false;

    // 描画中に記録していた値をリセットする
    lastPosition.x = null;
    lastPosition.y = null;
  }

  // マウス操作やボタンクリック時のイベント処理を定義する
  function initEventHandler() {
    const clearButton = document.querySelector('#clear-button');
    clearButton.addEventListener('click', clear);

    // 消しゴムモードを選択したときの挙動
    const eraserButton = document.querySelector('#eraser-button');
    eraserButton.addEventListener('click', () => {
      // 消しゴムと同等の機能を実装したい場合は現在選択している線の色を
      // 白(#FFFFFF)に変更するだけでよい
      // context.lineWidth = 50; // 線の太さ
      currentColor = '#FFFFFF';
    });

    // 鉛筆モードを選択したときの挙動
    const blackButton = document.querySelector('#black-button');
    blackButton.addEventListener('click', () => {
      // 消しゴムと同等の機能を実装したい場合は現在選択している線の色を
      // 白(#FFFFFF)に変更するだけでよい
      // context.lineWidth = 150; // 線の太さ
      currentColor = '#000000';
    });

    canvas.addEventListener('mousedown', dragStart);
    canvas.addEventListener('mouseup', dragEnd);
    canvas.addEventListener('mouseout', dragEnd);
    canvas.addEventListener('mousemove', (event) => {
      // eventの中の値を見たい場合は以下のようにconsole.log(event)で、
      // デベロッパーツールのコンソールに出力させると良い
      console.log(event);
      draw(event.layerX, event.layerY);
    });
  }

  // イベント処理を初期化する
  initEventHandler();
});