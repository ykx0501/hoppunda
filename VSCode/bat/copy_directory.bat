#==============================================================
# コピー先のディレクトリを決める
#==============================================================
# 今日の日付を取得
$now_day = Get-Date -Format "yyMMdd"

# 曜日を取得
$now_dayOfWeek = (Get-Date).dayOfWeek

if( $now_dayOfWeek -eq 6 ){
# 土曜なら当日のフォルダ名に格納
    $storage_folder = $now_day
} elseif ( $now_dayOfWeek -eq 7 ){
# 日曜なら前日のフォルダ名に格納
    $storage_folder = $now_day - 1
} else {
# 火曜/水曜以外は終了
    exit
}

#==============================================================
# コピー
#==============================================================
# コピー処理
Copy-Item  C:\work\VSCode\bat\Demo\コピーしたい\sample.txt C:\work\VSCode\bat\Demo\コピー先\$storage_folder