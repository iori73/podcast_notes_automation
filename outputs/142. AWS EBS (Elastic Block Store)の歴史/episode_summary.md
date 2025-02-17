## **基本情報**

- Spotify URL：[エピソードリンク](https://open.spotify.com/episode/6cxt8E0x254rML2t2t5MCp?si=UHSuATcpQ6KNARByouK2Rg)
- 公開日：2025年01月12日
- 長さ：36:41
- LISTEN URL：

## **要約**

このエピソードは、ある人物がAWSのハードウェアオフローディングについて話しています。彼は、AWSが新技術を取り入れる中で起きる変化を強調し、特にハードウェアオフローディングに焦点を当てています。AWSはそれに伴い、従来のソフトウェアベースのタスクを専用ハードウェアに移行していることがポイントです。例えば、EC2インスタンスではナイトロテクノロジーが活用され、ハードウェアの処理能力が最大限に活用されています。また、EBSサービスにおけるバーチャライゼーション機能の移行や、ネットワークにおける課題の解決にも取り組んでいます。このエピソードでは、技術的な内容が多く、新たなプロトコルであるSRDの導入や、TCPとの比較についても言及がありました。さらに、ストレージチームでの体験から、組織の変化やキャリアの転機についても触れられています。AWSの技術に興味がある方には興味深い内容となっています。是非、聴いてみてください。

## **目次**

00:01 AWS EBSの歴史について話す

00:35 子供部屋の準備と子育てエピソード

02:05 古いEBSブログ記事の紹介

04:23 ストレージサービスの歴史と発展

06:00 ストレージ性能の重要性

06:16 キューイング理論とシステムレイテンシー

09:57 キューイングセオリー

10:10 HypervisorとXen

13:06 組織論とチーム間コミュニケーション

15:44 縦割りとデータレプリケーション

17:40 チーム作成と長期的なプラン

18:10 ハードウェアオフローディングとナイトロ

20:40 ハードウェアオフロード

22:01 ネットワークのボトルネックとSRDプロトコル

23:32 ハイパフォーマンス用途のネットワークプロトコル

23:54 UDPとTCPの違い、順序保証について

25:59 新しいプロトコル開発の難しさ、QuickとHTTP3

28:12 EBSボリュームの使用とハードウェアの変遷

28:41 AWSにおけるキャリア成長とエンパワーメント

30:14 スケーリングとチームの重要性

32:29 APIの重要性とハードウェア・ソフトウェアの使い捨て性

35:37 技術力の宣伝

36:17 AWS EBSの歴史


## **文字起こし**

こんにちは Today I Learnedでは カリフォルニア ベイエリアで働くソフトウェア エンジニアが気になったトピック を紹介しながらトレンドを追っかけ ていきます 今日は AWS EBS Elastic Block Storage Service 発展の歴史について話して いきます まいともあきです サンフランシスコ にあるスタートアップでCTOとして 働いています 娘たちが大きくなってきたので 部屋を一つ子供部屋にして二段 ベッドを買ってあげました これで夜中に子供たちにキック されて目が覚めてしまうことも なくなるのかと思うと少し寂しい ま年子育てエンジニアです はい なんかね娘たちが結構今までこう お父さんと一緒に寝たいとか言って 下手すると3人まとめて1個のツイン だから2本のダブルベッドぐらい かなのサイズにぎゅうぎゅう詰め になって大体こう夜中に子供誰 かにキックされて目が覚めてしまう というのが通例だったんですけど 少しはマシにでもね真ん中の子 はまだたまに今日はお父さんと 寝るとか言って可愛いんですけど でも眠りがっていう感じです はいけどめちゃくちゃいいと思います 素敵だと思います はいでも二段ベッドは楽しいみたい であとはですねクリスマスプレゼント にプラネタリウムを買ってあげ たんですよ部屋の天井に映すやつ ですけどあれで結構もう完全に 子供部屋気に入って いいですね 楽しそうにしてます それはめっちゃなんか二段ベッド バンクですよあれもすごい子供 心をくすぐるツールですけどプラネタリウム もさらにそれを刺激するんで楽しい んじゃないかなと思いますけど はいそんな感じで今日は僕が持って きたネタなんですけどawsのEBSエラスティック ブロックストレージですねの歴史 について説明したブログ記事が あったんでこれをちょっと紹介したい と思います はい結構古いやつですよねネタの このブログ自体は割と EBS自体が EBSはそうですねすごい古いサービス ですねかなり初期にリリースされた awsの中でもかなり古いサービス の一つですこのブログ自体は今年 の8月ですね収録時点では24年年末 まだなんですけどこのエピソード が公開されるのは1月の予定なんで そういう意味では2024年去年リスナー の皆さんからすると去年の8月に 公開されたブログでawsの公式cto のブログかなただ著者自体はaws のプリンシパルエンジニアのマーク オルソンさんっていう方が書いた タイトルがcontinuous reinvention a brief history of block storage at awsっていう タイトル日本語で言うと簡単な awsの歴史って感じかなということで このマークさんはawsで13年働いている シニアプリンシパルエンジニア なんで多分いわゆるL8っていう ランクの人だと思うんですけど この人がかなり初期からEBSに携わって いたみたいでいろいろ昔の頃から どういうふうに発展して技術的に 改良されてきたのかっていうこと を説明してます ヤンヤン EBS自体はEC2とかそういう インスタンスとかにマウントできる ようなストレージですよね おだしょー そうですねいわゆる ストワークアタッチドストレージ なんだけどインスタンス上から 見るとまるでローカルにあるディスク のように扱えるっていう感じにな っていると思います歴史を簡単に おさらいすると初めてawsのサービス が公開されたのは2006年3月でS3 ストレージサービスが一番最初 の公開されたサービスです同じ 2006年の7月にSQSで8月にEC2EC2は 3番目のサービスですね翌2007年 にシンプルDBで最初のS3からおよそ 2年半後EC2から大体2年後の2008 年8月にEBSが公開されたっていう 感じです 深井 そうなんですねEC2より先に キューイングのほうがあったん ですねそれは知らなかったです おだしょー 意外とEC2辺りから爆発 的にヒットしたっていう感じです けど実は3番目だしEBS自体はだから 5番目のサービスになるのかなっていう 感じです初期はハードディスク 1台あたり数千Iopsで一つのEC2インスタンス にHundreds of thousandsだから数十万 Iopsの帯域を提供することができた と現在では140トリリオンIopsを 全体で提供しているとトリリオン っていくつだっけみたいな感じ ですけどメガがミリオンだから メガギガテラテラ140テラIopsって ことですかね 深井 すごいたくさん眼鏡性、デュラビリティよりも比較的って話ですけど、性能が重要になると。 なんでかっていうと直接インスタンスにアタッチされていて、ダイレクトにそのアプリケーションのパフォーマンスに影響があるっていうことですね。 ブログではですね、ちょっとキューイングセオリー行列理論の話が少し入ってますけど、 取り上げている例、よくある銀行の受付でお客さんが待っていて、お金を引き出したりとか預けたりとかするときの待ち行列の話をしてるんですけど、 ちょっとこれはめんどくさい話なんで、このPodcastでは深くつかまないんですけど、 肝はですね、行列、待ち行列、キューですね。いろんなシステム、いろんなとこにキューがあると全体としてシステムがレイテンシーに敏感になるというか、 レイテンシーのアートライヤーを制御しにくくなるっていうところがポイントかなと思います。 最初はですね、古い時代はハードディスクで、僕の記憶ではLacのEC2のインスタンスのハードウェアが載っているLacの同じLacにEBSのストレージサーバーが載っていて、 基本的に同じLacのストレージを使うみたいな感じだったと思います。 なるほど。 正確にいつの時代のことだったか覚えてないんですけど、僕はAmazonに入ったのは2012年なんで、その時期まだそういうシステムが多分あったって感じですね。 とにかく初期はハードディスクで、ハードディスクは遅いんでネットワークの心配はそんなにしなくてよかった。 それはどういうことなんですか。ネットワークの心配っていうのは。 つまりハードディスクがすごい遅いので、ネットワークがボトルネックにならないっていうことですね。 またあとジッターが大きいというか、最悪の場合のレイテンシーですね、テールレイテンシーがかなりでかいので、ハードディスクをそのまま使うと、 例えば1台だけとか使うと大変遅い場合が出てきちゃうんで、ディスクに分散して、すごい単純に言うとストライピングしてそのレイテンシーを隠していたわけですね。 ところが当然複数の顧客でディスクを共用しているので、ノイジーネイバー、騒がしい隣人っていう問題が出てきます。 このノイジーネイバーっていうのって聞いたことあります? ないですね。けど想像するに他人の使っているリソースで自分が影響を受けちゃうとかですかね。 そうですね。ハードディスクを共有してるんで、同じインスタンスを使っている他の顧客がめちゃめちゃ待機とかIops使っていると、 当然自分は大したことをしてないのに早いはずの処理がすごい遅くなってしまうことがあるっていう共有インスタンスでは問題になりがちな現象ですね。 はい。それで2011年頃からSSDが徐々に入ってきて、プロビジョンドIOなんていうサービスっていうのかな。 あらかじめこんだけの待機を保証しますよみたいな使い方もできるようになったんですけど、なかなかノイジーネイバー問題は直らなかったらしいです。 2012年頃は要は素朴なシステムで測定もかなり限られていたと。 だから改善するのにどこが悪いかっていうのを突き止めるために、まずありとあらゆるサブシステムのIOに測定ポイントを追加して、 システムを変更した時にカナリアテスト、カナリですね、なんかを流してその変更、改善なり修正の変更の性能への影響がどういうことになっているかっていうのを細かく測定できるようにまずしたという、 まず改善の第一歩として測定をいっぱいできるようにしたらしいです。 測定の結果、システム全体でQの数、さっき行列理論、キューイングセオリーの話で出てきましたけど、とにかくシステム内にQがいっぱい多すぎるんで、まずこれを減らさないといけないと。 それからHypervisorにXenを使ってたんですけど、Xenですね、これがEC2では十分な機能があったんだけど、 EBSのサーバーでもXenを使って仮想化とかなんとかの分離ですかね、してたと思うんですけど、とにかくストレージサーバーに使うには機能がXenは足りなかったと。 何が足りなかったんでしょうね。 ちょっとあんまり細かくは書いてなかったんですけども、改善したポイントとしては例えばディスク上のデータのレイアウトとかキャッシュラインの最適化とか、 非同期プログラミングを導入したっていうようなことがあったんで、たぶんその辺にあったんじゃないかな。 基本的に性能関連の機能っていうことなんですかね。 ストレージサーバーなんかちょっと違いますもんね、そもそも振る舞いがアプリケーションサーバーと、それが改善されたんでしょうね。 あとですね、なんかあんまりこの辺ちゃんと設定とかデザインの見直しをそれまでちゃんとやってなかったらしくて、 そのXenの設定がEC2向けのままで全然パフォーマンスチューニングされてなかったっていうことも書いてありました。 なので、それをちょっとチューニングしただけでかなり良くなったと。なんかね、キューのサイズとか、ストレージ向けのIOのキュー、IOキューの数とか、 1個1個のキューの最大の長さなんかも全然チューニングされてなくて、最初は64個しかキューが、システム全体で顧客ごとじゃなくて、システム全体で64個のIO待ちリクエストしかキューイングさせる。ことができなかったみたいなことが書いてありました。64回じゃもう全然足りないです。 そうですね。どうなってんだ。 そういうまあちょっと短期的な改善もいろいろやったんだけど、とにかくそのこの段階のまあだから 2012年13年頃の問題ってのはまずそのどこにパフォーマンスの問題があるのかあんまりよく分かって なかったんで測定を強化してでとりあえず短期的なソフトウェアの改善っていうのは前の パラメータチューニングとかその上で動くその デュラビリティエンジンって言ってましたけどまあ多分 ブロックをどういうふうに配置したり変えたり えっとまあエンコーディングしたりとかそういうところだと思うんですけどそういうところの改善を 主にしていたと。でさらに並行して長期的なアーキテクチャの変更の計画を いろいろ立てたって書いてました。でこの長期的な計画の詳細は触れられてなかったんですけど まあ1個面白いなぁと思ったのがですねこの分割して統治っていう セクションがこのブログ記事の中であってここはですねちょっと技術的な話じゃなくて どっちかというと組織論の話をしてました Amazonではあのよくトゥーピッツァーチームとかって言ってちっちゃめのチームであと APIマンデートってチームとチームの間で会議して相談 なるべくしないようにその代わりにAPIを決めてチームとチームの間はAPIで話しなさいと 簡単に言うとそういう方針なんですけどこれはフロントエンドとかコントロールプレーンみたいな チームにはうまく組織論としてあのうまく作用するんですけど データプレーン ちなみにこのコントロールプレーンとデータプレーンっていう用語もなんかもしかしたらあんまり耳慣れない人が多いですかね そうですねあんまり言わない気がしますけどはい そうですね元々なんかネットワークの用語っていうかソフトウェアデファインドネットワークが発祥の用語だと思うんですけど まあ分散コンピューティングクラウドの業界でもそのコントロールプレーンっていうのは簡単に言うと設定をするためのソフトウェア でデータプレーンっていうのは実際のお仕事をする部分ですねだから例えばそのストレージサービスの場合は コントロールプレーンっていうのは全体としてどういうリソースをどこに割り当ててこの顧客はどこにアクセスできるとか コンフィギュレーションをどういうふうに管理するとかまあそういうことをやっていてデータプレーンっていうのは実際にストレージの場合は例えば データの書き込みがありましたと書き込みをどういうパスどういうコンポーネントを通って最終的にディスクに書くわけですけど その時の実際にデータを書き込むまでの制御を司るところですね でこのデータプレーンの特にパフォーマンスチューニングとかをするっていうのは一種総合格闘技なわけですよ なんで機能ごとのとかレイヤーごとのチームだとうまくいかないとどうやら 例えば当然そのAWS EBSもクラウドのサービスなんでAPIフロントエンドがあって いろんなコンポーネントがあってディスクハードウェアのチームがあってファームウェアのチームがあってとかいろんなコンポーネントごとのチームはいるんですけど おそらくそういうチームごとそのチームとチームのコンポーネントの間はAPIで当然話してるんだけど そのチームごと個別にそれぞれパフォーマンスの問題を解決しようとしてもうまくいかないということだと理解しました 結局どうしたかっていうともうちょっと多分縦割りって言うとなんか聞こえが悪いですけど データレプリケーションとかデュラビリティとかスナップショットハイドレーションとか スナップショットハイドレーションっていうのは多分スナップショットの復元っていうことだと思うんですけど そういう特定の技術領域ただそのコンポーネントに縛られないで データレプリケーションって言っても当然いろんなプロトコルのスタックとか技術スタックをなんか串刺しで見るようなチームを作って 多分これがだからスタック横断って言うんですがあまり正直細かいことは書いてなかったんで結構想像も入ってるんですけど そういうテーマごとのチームを作って問題解決に当たったらしいです すごいですよねなんかハードウェアメーカーとかでもないのにこのレイヤーまでがっつりあるチームを作るっていうのはすごいし わかんないですけど例えばデータレプリケーションチームにずっといた場合はなんかもう本当にそこに詳しくなっていくんですよねきっと 僕も2000年頃1年ぐらいこのAWSの関連チームストレージの関連チームにいたんですけど正直そのハードウェア側だったんでソフトウェアの方は全然知らないというかわからないというのは正直なところですけど とにかくもうすべてのテックスタックのすべてのレイヤーでかなりいろいろすごいことをやっていますと そういうチームを作っていろんな長期的なプランをいろいろやるわけですね で1個大きいのがハードウェアオフローディングをするというところで2017年までEC2って全ハイパーバイザーで動いてたんですよね EBSのクライアントはハイパーバイザーの中で動いてたつまりソフトウェアで基本的に動いていました。 これが徐々に結論を言うと、ハードウェアオフローディングをします。 そこでキーになるテクノロジーがナイトロっていうやつで ハードウェアオフローディングって何ですか? つまりソフトウェアでやってた部分をハードウェアにやらせるようにするということですね。 なるほど。 ナイトロっていうのは元々はネットワークかな? EC2のインスタンス、少し戻って、ナイトロって何かというと 従来ソフトウェアでやられていた処理を ハードウェアでやる、さっき言ったハードウェアオフローディングなんですけど それがどうやっているかというと EC2のインスタンスにPCI Expressカードが刺さっていて その上にARM Linuxのボードが載っています。 PCIバスからネットワークだったり NVMeデバイス、ストレージのインターフェースが生えている。 それを全部Linuxベースのソフトウェアで制御する っていうテクノロジーなんですけど、通じてるかな? これオフロードって言ったときに Linuxじゃないってことですよね? Linuxのさらに下のレイヤーって EC2のインスタンス本体の方も普通はLinuxが多いじゃないですか Windowsとかも動かせるはずだけど Ubuntuとかが動いてるわけですよね。 そのインスタンスが動いているEC2のハードウェアの 物理ハードウェアに物理カード、PCI Expressカードが刺さっていますと そのカードには組み込みARM Linuxが載っている。 組み込みのLinux。 ホストとはPCIeで通信をしてるんですけど ネットワークの一番大きいのは HypervisorでやっていたVPC、バーチャルプライベートクラウドの ネットワークの振り分けパケットの処理みたいなのを 全部ハードウェアでやるようにしたと。 それが何が嬉しいかっていうと ホスト側の通常x86のCPUのサイクルを 今までHypervisorがVPCのパケットのデコードとかに ちょっとCPUのサイクルを取られてたんですけど それを全部顧客が100%使えるようになって レイテンシーに敏感な処理とかを 専用のハードウェアでやることができるという感じです。 ネットワーク向けのオフローディングが大成功したので ストレージデバイスのつまりEBSのサービスの いろんなバーチャライゼーションの機能とかが 前のHypervisorで動いてたんですが これをNitroに移行しようということをして これ自体は良かったらしいんですよね。 例えばHypervisorにあったソフトウェアで 管理されているキューをオフロードして 素早い処理ができたりとか ハードウェアで暗号化の処理ができるようになったので セキュリティ的にもいいことがある。 つまりHypervisorから暗号鍵にアクセスできないわけですね。 なのでホストのOSさらにHypervisorが ジェールブレイクされても 例えば暗号鍵を盗み出すことができない みたいな利点があるわけです。 そういう意味でいろいろ Nitro自体は成功だったんですけど そうすると今度はネットワークが ボトルネックになったと。 さっきですね EBSのストレージサーバーが同じ EC2と同じラックにあったと 僕の記憶なんでちょっと間違ってるかもしれないですけど 多分この時点では EBSは専用のラックで 何かの違う場所にある状態になっていると思います。 距離的に離れている。 距離的に離れている。 それだけじゃなくて多分複数の ラックになるEC2のサーバーから離れたところにある 複数のインスタンスから EBSのボリュームにアクセスされている っていう状態ですね。 だからネットワーク的にはちょっと複雑になってるわけです。 これがTCP IPだとうまくいかないっていうんで 独自開発のSRD スケアラブルリライアブルダイアグラムっていう ちょっと調べるとUDPベースの プロトコルっていうことらしいんですけど データグラムですか データグラム ダイアグラムじゃなくて このSRDっていうプロトコルが TCPより何が優れてるかっていうと TCPってもともとは 割と遅いタイムスケール ミリセカンド単位で動作する だからリトランスミットとか ウィンドウとか全部ミリセカンド単位で 基本的に動作するわけですけど データセンター内のネットワークが マイクロセカンドとか オーダーが一個でかいんで 用途として向かないということで それに合わせてチューニングされてる ちょっと調べると インフィニバンドとかって聞いたことあるか わかんないんですけど そういうハイパフォーマンス用途の ネットワークプロトコルっていうんですかね と似ている部分があるらしいです もう一個大きな違いは TCPと違って厳密な順序保証がされてるただUDPよりは信頼性があってパケットの到達性は保証されるんだけど順序は保証しないと。 なんでかっていうと順序を保証するところをトランスポート層に組み込んでしまうと それがいわゆるヘッドラインブロッキングっていって 一個パケットが詰まっただけでその後全員詰まってしまうっていう現象が起きるわけですね。 これが結構テイルレイテンシーに致命的なんでこれを防ぐために 順序保証はもう一個上のレイヤーでやるように。 まあこれはなるほどなあっていうかまあその上の特にハイパフォーマンスコンピューティングで 用途によって順序保証の厳密性って全然何か必要性が変わるわけですね。 例えばストレージだとパケットの到着順序が多少変わってもそのバリア命令って言うんですかね。 そのバリア命令って通じます? なんとなくあれですか。 メモリーバリアだったらCPUとかだと。 アクセス制御。 アクセス順序をこの瞬間の前後は入れ替えないでくれと。 それより後のものは後のもの同士前のもの同士で順番が入れ替わってもいいよっていう簡単に言うとそういうやつですけど そういう緩い順序保証でいい場合は上のレイヤーでやればいいじゃんと。 そうすることによってすごいレイテンシーが改善するということらしいです。 すごいですねよく考えますね。 要はこれだけのために新しいプロトコルをですね開発して このプロトコルを開発するっていうのは結構大変な。 GoogleとかもねQuickをあれってGoogleですよね。 Quickって確かね。 HTTP3と。 Quickも確かUDPベースですけどそういうのを作るのかなり大変だと思うんです。 ちなみにナイトロっていうのは2016年に買収したアナプナラボっていうところが作っていた製品ですね。 さらにストレージなんかはまさに僕がやってたところだと僕はファームウェアを開発するチームにいたんですけど もう普通のSSDをAmazonは買ってない。 全然ってわけじゃないですけど買ってなくてストレージサービス向けには生ナンドを買ってるんですね。 生ナンドで自前でもちろんね生産とか多分OEMって台湾とか中国でやってるんじゃないかなと思うんですけど 普通はフラッシュトランスレーションレイヤーっていうウェアリビリングとかエラー訂正をやってるところがあるわけですけど これを全部Linux上で全部じゃないかもしれないけど自分で開発したりとかして とにかくなんかもう上から下まで全部自前でやってるという恐ろしい会社です。 すごいですよね。なるほど。 さらになんかこういう改善をしたんだけど古いハードディスクベースのサーバーが何千台も稼働してたともったいないと だからこの稼働してるサーバーももうちょっとなんか改善したいっていうんでこれびっくりしたんですけど サーバーの空いてるハードウェアの空いてるスペースにリフォーメンテープとフックで後付けでSSDを固定して このサーバーをアップグレードしたと。めっちゃ穴黒くんじゃないですか。そうなんですよね。 いやーすごいですよね。すごい。なんか結構泥臭いことも。そうなんですよね。 Amazonのすごいのはこういう泥臭いところを結構地道にやってたりするっていうところですよね。 あとすごいのはこの今までやってきたもの全部の改善っていうのはサービスを稼働状態のままダウンさせることなく全部やっていると。 なので2008年にEBSがサービス公開されてからずっと最初から使われているEBSボリュームもあるらしいんですけど そういうやつは実際に本当に使われているかどうかはわかんないですけど いろんな何百もの違うストレージサーバーEBSサーバー何世代ものハードウェアを渡り歩いていると サービス無停止で渡り歩いているということらしいので。すごいですね。 ハードウェアは使い捨てというか乗り換えるものであると。ソフトウェアはハードウェアを渡り歩くということですね。 そんな感じでだんだん終わりの方に近づいているんですけど こういうサービス改善を振り返ってみてその筆者自身のキャリアの転換っていうのもありましたと。 これは筆者自身がAWSに入るまではスタートアップとかずっと少人数で開発とかやっていたらしいんですよね。 だから割と自分でやる系の人だったんだけど、AWSに入ってしばらくしてこの筆者の人が組織上のボトルネックになってるよお前って同僚にあるとき言われてたらしいんですね。 その時点でも多分それなりに偉いエンジニアだったんだろうと思うんですけど すべての設計とかコードレビューとかエスカレーションにこの人マークさんが関わっていたらしいんですね。 それでボトルネックになってこの人はうんって言わないと仕事前に進まないみたいなそういう人になっていたんだけど ある時何か会議室で数人のエンジニアと共同でデバッグみたいなことをしていたら 同僚がポッとそれを解決してそれを見て、自分が全部やらなくてもいいんだということで、他の人をエンパワーする、権限を異常することが大事だと気づいたっていう、まあちょっといい話っぽいことが書いてありました。 スケーリングパフォーマンスですね、人間の。EBSだけじゃなくて。EBSだけじゃなくて、人間組織。チーム。 スケーリングするという感じで、そういうフィッシャー自身の振り返りも書いてあったということで、だからこのブログが公開された時点で、大体16年?16年間か。 この著者の人が13年っていうんだから、だからサービス開始後3年ぐらいでEBSに多分チームに入って、ずっとそこでキャリアを積んで、今シニア、プリンシパル、上級、主管、エンジニアとかそんな感じだと思うんですけど、 叩き上げって感じですね、すごいなったということです。 すごいですね。このブログポストは、さっき最初言ってましたけどCTOの人がやってる。 はいはい、そうですね。 ワーナーさん。 大分前にフルアルアーキテクトの回で取り上げたCTOの人のブログなんですけど、この文章を書いたのはマークさんということらしいですね。 最初にワーナーさんの前書きみたいなのがついていて、本文はマークさんが書いたと。 だからかなり信頼もされているってことですよね、このCTOの人に。 そうだと思います。そんな感じで、僕的に学びを少しですね、駆け出してみたんですけど、まず実装っていうのは変わるもの、移ろうものだと。 いいAPIっていうのはずっと使われる。サービスのスケーラビリティっていうのは、実装レベルのスケーラビリティもそれなりには重要なんですけど、API自体のスケーラビリティのほうがはるかに重要で、 APIとかがそのサービスを停止しないで実装を入れ替えられるというところまで考えてAPIなりが、あと初期の実装が作られていれば、後々直していける、長続きさせることができると。 そういう意味ではハードウェアも使い捨てだし、ソフトウェアも使い捨てであると。いいAPI、だからレイヤーとしてはハードウェア、ソフトウェアの上にAPIが来るみたいな感じかな。 ある意味その寿命という、望まれるべき寿命の順で言うとそういう感じなのかなっていうふうに思いました。 あと細かい測定、特に分散コンピューティングの環境ってすごい後から測定するのってめちゃめちゃ難しいし、ボトルネックとかがどこにあるのかって本当に全然わからないんで、今でもそうだし、メタでもそうだし、AWSもそうですけども、とにかくありとあらゆるポイントに測定が入ってます。 とても重要で、測定しっかりできることで段階的なインクリメンタルな実験とか変更ができるので、改善がやりやすいですね。っていうことと、ちょっとさっきの実装は移ろうって言いましたけど、ハードウェアは使い捨て、ソフトウェアはハードウェアを渡り歩く。 あとそういう意味ではデータはAPIと似ているところがあると思っていて、データは一般的にはソフトウェアを渡り歩く。データが一番価値のある資産だっていう場合も結構多いのかなって思いました。 データベースの設計というかテーブル設計とかもやっぱり最初にしっかりとやった方がいいですね。なかなか変えるの大変だし後から。 あとは行列理論という意味ではボトルネックを改善すると必ず次のボトルネックが現れると。これはもう数学的真理なんでボトルネックをいつまで経っても必ず何かしらボトルネックがあるっていう。つまり常に我々の仕事はなくならないみたいな感じで。 はい。いまいちブログ本体とあまり関係ないまとめだったような気もしますけど、そんなことをつらつらと読みながら思いました。今井さん的にはどうですかね。今井さんの守備範囲からするとレイヤーが低すぎだったかもしれないですけど。 面白い内容です。やっぱり普段この辺は全部抽象化されてAWSを使う側なんで全くその裏側でどうなっているかあまり理解してないですけど、こういうのを読むとすごいんだなって思うところはあるし。 というかこのブログは誰に向けて書いたんだろうっていうのはちょっと今思いました。これ読んで確かにすげーなって思うんですけど、顧客の多くはこれを果たして読むのかどうかとかよくわかんないなっていう。これを見るとすげーことやってるし、確かにだから安心して使えるっていうのは感じました。 そうですね。宣伝はある意味技術力の宣伝っていうところもあると思うんですけど、純粋にこういうブログが面白いですよね。面白いと思います。あとリクルーティングっていう目的もそういえばありますね。 あーなるほど。こういうふうなことに取り組む。いるのかな?けど世の中でここまでの。そう多くはなさそうな気もするんですけども、まあけどそれでも価値はありますね、と思います。 はい。ということで今日はAWS EBSの歴史について話しました。 よかったら感想をハッシュタグシャープTILFMでつぶやいてください。またお使いのポッドキャストアプリでもいいね、お気に入り、コメントなどお待ちしています。 ありがとうございました。

## **English Summary**

This episode features a discussion with somebody who works on hardware offloading at AWS. He highlights the changes that AWS is driving in adopting new technologies and focusing in particular on hardware offloading. He makes the point that AWS is increasingly moving traditionally software-based tasks into dedicated hardware. He gives examples including the use of Nitro technology in EC2 instances which allows for more of the hardware's processing power to be used. He also discusses the work being done on moving virtualization functions into the EBS service and work on solving challenges in networking. There is a lot of technical content in this episode including the adoption of a new protocol SRD and a comparison of that with TCP. The conversation also covers themes of organizational change and career transitions, reflecting on the speaker's experience in the storage team. Altogether this should be an interesting episode for those interested in the technology at AWS and is well worth a listen.


## **English Transcription**

**Hello, Today I Learned**

In this episode, we're going to cover a topic that's near and dear to my heart as a software engineer working in the San Francisco Bay Area, California. It's the history behind AWS EBS or Elastic Block Storage Service. My name is Mai Tomoki. I'm the CTO of a startup here in San Francisco.

I recently bought a bunk bed for my kids' room because they have been getting bigger. So I thought maybe that would save me from getting kicked awake in the middle of the night. Now I'm a little sad about it because I won't have those moments anymore. But that's the life of a parent with a career in engineering.

Anyways, the girls really liked it. I also bought them a planetarium that projects onto the ceiling of their room. They really loved that. So that was a win-win. It's really fun for them.

So, today's topic, as mentioned earlier, is EBS - a block storage service in AWS. It's pretty old. EBS is one of the oldest services on AWS. It was released very early on. The blog post itself was published in August of this year, 2024. 

The author of the blog post, Mark Olson, is a Principal Engineer at AWS. He’s been with AWS for thirteen years. He's probably at the L8 level, which is pretty high up. And he was involved in EBS from the very beginning. So he talks about some of the early technical improvements and developments of EBS.

EBS is storage that can be mounted to instances like EC2. It can be treated like a local disk from the instance's perspective.

Here's a quick history of AWS services:

* March 2006: AWS launched its first service, S3, which is a storage service.
* July 2006: SQS was released.
* August 2006: EC2 was released, which was the third service.
* 2007: SimpleDB was released.
* August 2008: EBS was released, about two and a half years after S3 and about two years after EC2.

Initially, EBS used hard disk drives (HDDs) with a few thousand IOPS per drive. It could provide hundreds of thousands of IOPS of bandwidth to a single EC2 instance. Today, AWS provides 140 trillion IOPS in total.

Around 2011, SSDs started to become more common, along with provisioned IOPS, which allowed users to specify the minimum amount of IOPS they needed. However, the noisy neighbor problem was still a problem.

In 2012, AWS had a pretty basic monitoring system, so in order to improve performance, they added measurement points to all of the subsystems' I/O. They also did a lot of canary testing to measure the impact of performance changes.

They found that there were too many queues in the system, so they needed to reduce that. They were also using Xen as the hypervisor, which was good enough for EC2, but it wasn't good enough for the EBS servers.

They improved the performance of the EBS servers by optimizing the data layout on the disks, the cache line size, and introducing asynchronous programming. They also found that they hadn't done a good job of configuring and designing the Xen settings. So, they made some optimizations there as well.

In addition to these short-term improvements, they also started planning for some long-term architectural changes. One interesting thing they did was create a section in the blog post called "divide and conquer." This section wasn't about technical stuff but rather about organizational theory.

At Amazon, they have something called "two-pizza teams," which are small teams that are encouraged to make decisions on their own using APIs instead of having meetings with other teams. This works well for teams working on things like frontend and control plane, but it doesn't work as well for data plane.

In the context of EBS, the data plane is responsible for things like writing data to disks. This is a complex task that requires a lot of expertise in different areas. So, AWS created cross-stack teams to work on specific technical areas, such as data replication, durability, and snapshot hydration.

In 2017, all EBS clients were running in hypervisors. Gradually, they started to move to hardware offloading, which is when software functions are moved to hardware.

A key technology in this process was Nitro, which is a PCI Express card that plugs into an EC2 instance. The card has an ARM Linux board on it, which controls the network, NVMe devices, and storage interfaces.

Nitro offloads a lot of the tasks that used to be done by the hypervisor, such as network packet processing. This frees up the CPU cycles on the host, which can be used for latency-sensitive tasks.

The network offloading was so successful that AWS decided to move the virtualization functions for EBS to Nitro as well. This also worked well. For example, they were able to offload the queues that were managed by software in the hypervisor, which resulted in faster processing. They were also able to do encryption in hardware, which improved security.

However, the network became a bottleneck. The EBS storage servers were no longer in the same racks as the EC2 instances. They were in separate racks in a different location. And multiple EC2 instances were accessing EBS volumes from different racks.

This made the network traffic more complex. TCP/IP wasn't working well, so AWS developed their own protocol called SRD (Scalable Reliable Datagram). SRD is a UDP-based protocol that is better than TCP for this application because it has lower latency and is more reliable.

Another big difference between TCP and SRD is that SRD doesn't guarantee strict ordering. This means that packets can arrive out of order, but they are guaranteed to arrive. This is important for EBS because it doesn't matter if the packets arrive out of order as long as they eventually all arrive.

AWS also started using raw NAND flash memory for storage instead of buying SSDs from other companies. They developed their own flash translation layer and other software to manage the NAND flash.

Amazingly, AWS was able to upgrade some of their old HDD-based servers by attaching SSDs to them using Velcro.

All of these improvements were made without taking the EBS service down. So, there are some EBS volumes that have been in use since the service was launched in 2008.

The author of the blog post, Mark Olson, reflects on his own career journey in the context of these service improvements. He started out working on small teams at startups. When he joined AWS, he realized that he was becoming an organizational bottleneck because he was involved in every design decision, code review, and escalation.

One day, he was debugging something with a few other engineers in a conference room and one of his coworkers solved the problem without him. This made him realize that he didn't have to do everything himself and that it was important to empower others.

Olson also learned that implementations change over time, but good APIs last. The scalability of a service is more important at the API level than at the implementation level. This is because APIs allow you to swap out implementations without taking the service down.

In summary, hardware is disposable, software is reusable, and APIs are the most important layer.

Olson also emphasizes the importance of measurement, especially in a distributed computing environment. It's important to have metrics in place to identify bottlenecks and measure the impact of changes.

Finally, Olson reminds us that as we improve one bottleneck, another one will always appear. This means that our work is never done.

I hope you enjoyed this episode of Hello, Today I Learned. If you did, please tweet about it using the hashtag #TILFM. You can also like, favorite, or comment on this episode on your podcast app. Thanks for listening!

