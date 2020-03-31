from rest_framework.routers import DefaultRouter

from core.views import BookListViewSet, JournalListViewSet

router = DefaultRouter()

router.register(r'books', BookListViewSet)
router.register(r'journals', JournalListViewSet)

urlpatterns = router.urls
