from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from data.models import Ipldata,Iplmatcheswondata,Iplmatchesplayedvswon,Ipltopeconomicalbowlers, Iplextrarunsconcededperseason
from .serializers import IpldataSerializer, IplmatcheswondataSerializer, IplmatchesplayedvswonSerializer,IpltopeconomicalbowlersSerializer, IplextrarunsconcededperseasonSerializer

class IpldataListApiView(APIView):
    @staticmethod
    def get(request,*args,**kwargs):
        ipldata = Ipldata.objects.all()
        serializer = IpldataSerializer(ipldata, many=True)
        return Response(serializer.data,status = status.HTTP_200_OK)

    @staticmethod
    def post(request,*args,**kwargs):
        data = {
            'title': request.data.get('title'),
            'year': request.data.get('year'),
            'matches': request.data.get('matches')
        }

        serializer = IpldataSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class IplmatcheswondataListApiView(APIView):
    @staticmethod
    def get(request,*args,**kwargs):
        iplmatcheswon = Iplmatcheswondata.objects.all()
        serializer = IplmatcheswondataSerializer(iplmatcheswon, many=True)
        return Response(serializer.data,status = status.HTTP_200_OK)

    @staticmethod
    def post(request,*args,**kwargs):
        data = {
            'title': request.data.get('title'),
            'teamname': request.data.get('teamname'),
            'teamabbr': request.data.get('teamabbr'),
            'matcheswon': request.data.get('matcheswon')
        }

        serializer = IplmatcheswondataSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class IplmatchesplayedvswonListApiView(APIView):
    @staticmethod
    def get(request,*args,**kwargs):
        iplmatchesplayedvswon = Iplmatchesplayedvswon.objects.all()
        serializer = IplmatchesplayedvswonSerializer(iplmatchesplayedvswon, many=True)
        return Response(serializer.data,status = status.HTTP_200_OK)

    @staticmethod
    def post(request,*args,**kwargs):
        data = {
            'title': request.data.get('title'),
            'teamname': request.data.get('teamname'),
            'teamabbr': request.data.get('teamabbr'),
            'year': request.data.get('year'),
            'matchesplayed': request.data.get('matchesplayed'),
            'matcheswon': request.data.get('matcheswon')
        }

        serializer = IplmatchesplayedvswonSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class IpltopeconomicalbowlersListApiView(APIView):
    @staticmethod
    def get(request,*args,**kwargs):
        ipltopeconomicalbowlers = Ipltopeconomicalbowlers.objects.all()
        serializer = IpltopeconomicalbowlersSerializer(ipltopeconomicalbowlers, many=True)
        return Response(serializer.data,status = status.HTTP_200_OK)

    @staticmethod
    def post(request,*args,**kwargs):
        data = {
            'title': request.data.get('title'),
            'year': request.data.get('year'),
            'topeconomybowler': request.data.get('topeconomybowler'),
            'teamname': request.data.get('teamname'),
            'matches': request.data.get('matches'),
            'economy':  request.data.get('economy')
        }

        serializer = IpltopeconomicalbowlersSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class IplextrarunsconcededperseasonApiView(APIView):
    @staticmethod
    def get(request,*args,**kwargs):
        iplextrarunsconceded = Iplextrarunsconcededperseason.objects.all()
        serializer = IplextrarunsconcededperseasonSerializer(iplextrarunsconceded, many=True)
        return Response(serializer.data,status = status.HTTP_200_OK)

    @staticmethod
    def post(request,*args,**kwargs):
        data = {
            'title': request.data.get('title'),
            'year': request.data.get('year'),
            'extras': request.data.get('extras')
        }

        serializer = IplextrarunsconcededperseasonSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
"""
class IpldataDetailApiView(APIView):
    @staticmethod
    def get_ipl(ipl_id):
        # Just a helper to return data accordingly to the id handed out.
        try:
            return Ipldata.objects.get(id=ipl_id)
        except Ipldata.DoesNotExist:
            return None

    def get(self, request, ipl_id, *args, **kwargs):
        ipl = self.get_ipl(ipl_id)
        if not ipl:
            return Response(
                {'res': 'IPL NOT FOUND'},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = IpldataSerializer(ipl)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, ipl_id, *args, **kwargs):
        ipl = self.get_ipl(ipl_id)
        if not ipl:
            return Response(
                {'res': 'IPL NOT FOUND'},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = IpldataSerializer(instance=ipl,
                                       data=IpldataListApiView.post(request).data,
                                       partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, ipl_id, *args, **kwargs):
        ipl_id = self.get_ipl(ipl_id)
        if not ipl_id:
            return Response(
                {'res': 'IPL NOT FOUND'},
                status=status.HTTP_400_BAD_REQUEST
            )
        ipl_id.delete()
        return Response(
            {'res': 'IPL DELETED'},
            status=status.HTTP_200_OK
        )
"""