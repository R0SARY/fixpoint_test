# fixpoint_test

## 仕様に関して
今回の出力は、ホスト名別のアクセス件数の表示、時間ごとのアクセス件数の表示の順に行いました。  
また、複数のファイルの入力に関して、どのファイルを読み込めばいいのかわからなかったので、今回は、/var/log/httpdディレクトリの直下にあるファイル全てを対象にとりました。  
課題4は解けませんでした。

## 実行方法
$python fixpoint_test.py  
と入力することで、ファイルを実行することができます。  
また、課題3である、期間の指定は上記の実行コマンドに、"-t"、"--time"オプションをつけることで指定を行うことができます。
その際のformatは"YEAR/MONTH/DAY YEAR/MONTH/DAY"となっており、1つ目の年月日は期間の始まり、2つ目の年月日は期間の終わりを表しています。
