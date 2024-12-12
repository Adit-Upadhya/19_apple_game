# Ａ－１最初）各種インポート処理
import pygame
from pygame.locals import QUIT, KEYDOWN, K_LEFT, K_RIGHT
import sys
import random
# Ｃ－３７playerから）プレイヤークラスのインポート
from player import Player
# Ｅ－５３itemから）アイテムクラスのインポート
from item import Item

# Ｂ－１４最初）ゲームの制限時間：一旦20とする
# Ｈ－７５最初、itemへ）ゲームの制限時間を長くする
MAX_TIME = 200
# Ｂ－１５）アイテムリスト(1,1,1,1,1,1,1,1,2,3,4)
# 1:リンゴ、2:金のリンゴ、3:ハリネズミ、4:岩
ITEM_LIST = (1,1,1,1,1,1,1,1,2,3,4)
               
# Ａ－２）Pygameの初期化処理
pygame.init()
# Ａ－３）キーの受付間隔
pygame.key.set_repeat(5, 5)
# Ａ－４）表示用の画面
surface = pygame.display.set_mode([800, 600])
# Ａ－５）一定間隔処理用
clock = pygame.time.Clock()
# Ａ－６）ウィンドウタイトル「*** APPLE GAME ***」
pygame.display.set_caption('***APPLE GAME***')

# Ｂ－１６）背景読み込み
bg = pygame.image.load('image/bg.png')
# Ｇ－６８最初）フォントを指定（Arial / Arial Black）
game_font = pygame.font.SysFont('Arial Black', 32)

# Ａ－７）メイン処理
def main():
    # Ｂ－１７）アイテムのリスト
    item_list =  []
    # Ｂ－１８）ゲームのカウンター
    game_count = 0
    # Ｂ－１９）スコア
    score = 0
    # Ｂ－２０）ゲームオーバーフラグ
    is_gameover = False
    # Ｂ－２１）プレイヤーライフ
    player_life = 3

    # Ｃ－３８）プレイヤーのインスタンスを作成する
    player = Player()

    # Ａ－８）ゲームのメインループ
    while True:
        # Ｂ－２２）ゲームのカウンターを１加算
        game_count += 1

        # Ａ－９）イベント処理ループ
        for event in pygame.event.get():
            # Ａ－１０）終了処理
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            # Ｄ－４３playerから）キーダウン処理
            elif event.type == KEYDOWN:
                # Ｄ－４４）ゲームオーバーでない場合
                if not is_gameover:
                    # Ｄ－４５最後）右キー、左キーの時にプレイヤーの移動
                    if event.key == K_RIGHT:
                        player.move(2)
                    elif event.key == K_LEFT:
                        player.move(-2)
                    
                    

        # Ｅ－５４）ゲームオーバーでない場合
        if not is_gameover:
            # Ｅ－５５）一定間隔ごとに
            if game_count % 30 == 0:
                # Ｅ－５６）ランダムにアイテムNoを決定
                no= random.choice(ITEM_LIST)
                # Ｅ－５７）アイテムのインスタンスを作成
                new_item = Item(no)
                # Ｅ－５８）アイテムリストに追加する
                item_list.append(new_item)
            # Ｆ－６７itemから、最後）すべてのアイテムの落下
            for item in item_list:
                item.fall()
            # Ｈ－８８playerから、最後）プレイヤーとアイテムのヒットチェック    
            score, player_life = player.hit_check(item_list, game_count,score)

        # Ｂ－２３）画面を黒で塗りつぶす
        surface.fill((0, 0, 0))
        # Ｂ－２４最後）背景の描画
        surface.blit(bg, (0, 0))
        
        # Ｅ－５９最後）アイテムの描画
        for item in item_list:
            item.draw(surface)
        # Ｃ－３９最後）プレイヤーの描画
        player.draw(surface, game_count)
        # Ｇ－６９）残りタイムの算出：（MAXタイム - アイテム数）で算出
        now_time = MAX_TIME - len(item_list)
        # Ｇ－７０）タイムを表示
        time_info = game_font.render(f'time: {now_time:4}',
                                    type,(0, 0, 255))
        surface.blit(time_info, (600, 550))        
        # Ｇ－７１）スコアを表示
        score_info = game_font.render(f'score : {score:6}',
                                      True, (250, 100, 0))
        surface.blit(score_info, (570, 0))
        # Ｇ－７２）タイムかライフが０になったら、ゲームオーバーにする
        if now_time <= 0 or player_life <= 0:
            is_gameover = True        
        # Ｇ－７３）ゲームオーバーの場合
        if is_gameover:
            # Ｇ－７４最後）ゲームオーバーの表示
            over_info = game_font.render('GAME OVER',
                                         True,(200, 0 ,0))
            surface.blit(over_info, (300, 0))
            

        # Ａ－１１）描画更新処理
        pygame.display.update()
        # Ａ－１２）一定時間処理
        clock.tick(100)

# Ａ－１３最後）メイン処理の呼び出し

if __name__ == '__main__':
    main()

