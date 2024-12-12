# Ｃ－２５最初）各種インポート処理
import pygame

# Ｃ－２６）プレイヤークラス
class Player:

    # Ｃ－２７）コンストラクタ
    def __init__(self):
        # Ｃ－２８）プレイヤーの画像を作成（同じサイズになるように調整）
        self.image_l = pygame.image.load('image/cat_l.png') 
        self.image_r = pygame.image.load('image/cat_r.png') 
        self.image = self.image_r
        # Ｃ－２９）ヒット時の画像
        self.hit_image = pygame.image.load('image/bang.png')
        # Ｃ－３０）ライフの画像
        self.life_image = pygame.image.load('image/heart.png')
        # Ｃ－３１）画面上の位置
        self.pos_x = 370
        self.pos_y = 450
        # Ｃ－３２）ライフ
        self.life = 3
        # Ｃ－３３）HITマーク表示時間
        self.hitmark_time = -1

    # Ｃ－３４）プレイヤー関係の画像を描画する処理
    def draw(self, surface, game_count):
        # Ｃ－３５）プレイヤー画像を描画
        surface.blit(self.image, (self.pos_x, self.pos_y))
        # Ｃ－３６mainへ）ライフの描画
        for i in range(self.life):
            surface.blit(self.life_image,(60*i,10))
        # Ｉ－９６下から）HITマーク表示時間が０以上で、
        # ゲームカウンタがHITマーク表示時間より短い間
        if self.hitmark_time > 0 and game_count <= self.hitmark_time:
            # Ｉ－９７）HITマークを表示する
            surface.blit(self.hit_image, (self.pos_x, self.pos_y))
        # Ｉ－９８）ライフが０以下の場合も
        if self.life <= 0:
            # Ｉ－９９最後）HITマークを表示する
            surface.blit(self.hit_image, (self.pos_x, self.pos_y))
        
    # Ｄ－４０最初）移動処理
    def move(self, step):
        # Ｄ－４１）移動距離に合わせて移動する
        self.pos_x += step
        # Ｄ－４２mainへ）移動方向によって、画像の向きを変える
        if step > 0:
            self.image = self.image_r
        else:
            self.image = self.image_l      
        
    # Ｈ－８３itemから）アイテムとの当たり判定処理
    def hit_check(self, item_list, game_count, score):
        # Ｈ－８４）プレイヤー画像の四角形
        player_rect = self.image.get_rect()
        # Ｈ－８５）当たり判定を、画像の四角よりやや小さくする
        pos_x = self.pos_x + 15
        pos_y = self.pos_y + 15
        width = player_rect.width - 30
        height = player_rect.height - 30
        # Ｈ－８６）アイテムの数だけ繰り返す
        for item in item_list:
            result = item.hit_check(pos_x,pos_y, width, height)
            
            # Ｉ－９１itemから）ハリネズミか岩と当たった場合
            if result == 3 or result ==4:
                # Ｉ－９２）ライフを減らす
                self.life -= 1
                # Ｉ－９３）ヒットマーク表示時間を今から一定カウント後に設定
                self.hitmark_time = game_count + 100
            # Ｉ－９４）リンゴと当たった場合
            elif result == 1:
                score += 1
            # Ｉ－９５上へ）金のリンゴと当たった場合
            elif result == 2:
                score += 3
            
        # Ｈ－８７mainへ）スコアとライフを戻り値にする（タプル型）
        return score, self.life

