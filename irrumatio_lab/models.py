from django.db import models


class Actress(models.Model):
    actress_bid = models.CharField(max_length=20)  # 标识（可能是英文名）
    actress_name = models.CharField(max_length=20)  # 番号

    def __str__(self):
        return self.actress_name


class ProductionEvaluation(models.Model):
    overall_mark = models.SmallIntegerField(null=True, blank=True, default=0, help_text='总评')  # 总评/10
    actress_mark = models.SmallIntegerField(null=True, blank=True, default=0)  # 女优评分
    irrumatio_times = models.IntegerField(null=True, blank=True, default=0)  # 次数
    irrumatio_cum_times = models.IntegerField(null=True, blank=True, default=0)  # 发射数
    irrumatio_throat_cum_times = models.IntegerField(null=True, blank=True, default=0)  # 喉奥发射数
    irrumatio_duration_min = models.IntegerField(null=True, blank=True, default=0)  # 时间 分钟
    spit_amount = models.SmallIntegerField(null=True, blank=True, default=0)  # 唾液量
    spit_sound = models.SmallIntegerField(null=True, blank=True, default=0)  # 唾液音
    puke_reaction = models.SmallIntegerField(null=True, blank=True, default=0)  # 呕吐反应
    speed = models.SmallIntegerField(null=True, blank=True, default=0)  # 速度
    depth = models.SmallIntegerField(null=True, blank=True, default=0)  # 深度
    cock_level = models.SmallIntegerField(null=True, blank=True, default=0)  # jb水平
    puke_amount = models.SmallIntegerField(null=True, blank=True, default=0)  # 呕吐物量


class ProductionAddons(models.Model):
    cover_img = models.CharField(max_length=200, null=True, blank=True)
    dmm_link = models.CharField(max_length=200, null=True, blank=True)


class ReviewImg(models.Model):
    review_img_link = models.CharField(max_length=200)
    production_addons = models.ForeignKey(ProductionAddons, on_delete=models.CASCADE)


class Production(models.Model):
    production_bid = models.CharField(max_length=20)  # 番号
    production_name = models.CharField(max_length=200)  # 名称
    pub_date = models.DateField(null=True, blank=True)  # 发行日期
    actresses = models.ManyToManyField(Actress)
    production_evaluation = models.OneToOneField(
        ProductionEvaluation,
        on_delete=models.CASCADE,
    )
    production_addons = models.OneToOneField(
        ProductionAddons,
        on_delete=models.CASCADE,
    )
    official_review = models.TextField(null=True, blank=True)  # 官方评论
    lab_review = models.TextField(null=True, blank=True)  # 研究所评论

    def __str__(self):
        return self.production_name




