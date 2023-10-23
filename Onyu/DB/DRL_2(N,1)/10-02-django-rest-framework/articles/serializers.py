from rest_framework import serializers
from .models import Article, Comment


class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'content',)


class CommentSerializer(serializers.ModelSerializer):
    # 클래스 안에서 새롭게 사용할 클래스를 지정해줌
    class ArticleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = ('title', )
            
    # override -> 기존에있던 meta의 read_only_fields가 적용되지 X
    article = ArticleSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
        # read_only_fields = ('article', )


class ArticleSerializer(serializers.ModelSerializer):
    # 이름 변경 안됨 // models.py에서 related_name 에서 지정해주어야함
    comment_set = CommentSerializer(many=True, read_only=True)

    # 새로운 필드 지정 - 이름 아무거나 가능
    # article.comment_set.count() 을 serializers 문법에 적용해주기 = source~~
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)

    class Meta:
        model = Article
        fields = '__all__'