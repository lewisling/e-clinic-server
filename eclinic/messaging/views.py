from rest_framework.views import APIView
from rest_framework.response import Response

from .models import MessageToken
from .serializers import MessageSerializer

class MessageTokenList(APIView):

	def post(self, request, format=None):
		"""
		create a message token for an existing user
		"""
		serializer = MessageSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MessageTokenDetail(APIView):
	def get_object(self, id):
		try:
			return MessageToken.objects.get(id = id)
		except MessageToken.DoesNotExist:
			raise Http404

    def put(self, request, id, format=None):
    	"""
    	update a message token
    	"""
    	messageToken = self.get_object(id)
    	serializer = MessageSerializer(messageToken, data = request.data)
    	if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    