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