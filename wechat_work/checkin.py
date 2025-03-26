from typing import Dict, Any, List, Optional
from datetime import datetime
from .client import WeChatWorkClient

class CheckinAPI:
    """Check-in API"""
    
    def __init__(self, client: WeChatWorkClient):
        self.client = client
    
    def get_checkin_data(
        self,
        open_checkin_data: List[Dict[str, Any]],
        open_checkin_type: int = 3
    ) -> Dict[str, Any]:
        """
        Get check-in data
        
        Args:
            open_checkin_data: List of check-in data
            open_checkin_type: Check-in type (1: all, 2: late, 3: early leave, 4: both late and early leave)
            
        Returns:
            Check-in data
        """
        return self.client.post_json("checkin/getcheckindata", json_data={
            "opencheckindata": open_checkin_data,
            "opencheckintype": open_checkin_type
        })
    
    def get_checkin_option(self, datetime: datetime) -> Dict[str, Any]:
        """
        Get check-in option
        
        Args:
            datetime: Date time
            
        Returns:
            Check-in option
        """
        return self.client.post_json("checkin/getcheckinoption", json_data={
            "datetime": datetime.strftime("%Y-%m-%d %H:%M:%S")
        })
    
    def get_checkin_schedule_list(
        self,
        start_time: datetime,
        end_time: datetime,
        user_ids: List[str]
    ) -> Dict[str, Any]:
        """
        Get check-in schedule list
        
        Args:
            start_time: Start time
            end_time: End time
            user_ids: List of user IDs
            
        Returns:
            Schedule list
        """
        return self.client.post_json("checkin/getcheckinschedulist", json_data={
            "starttime": start_time.strftime("%Y-%m-%d %H:%M:%S"),
            "endtime": end_time.strftime("%Y-%m-%d %H:%M:%S"),
            "useridlist": user_ids
        })
    
    def set_checkin_schedule_list(
        self,
        schedule_list: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """
        Set check-in schedule list
        
        Args:
            schedule_list: List of schedules
            
        Returns:
            Operation result
        """
        return self.client.post_json("checkin/setcheckinschedulist", json_data={
            "schedulelist": schedule_list
        })
    
    def get_checkin_month_data(
        self,
        start_time: datetime,
        end_time: datetime,
        user_ids: List[str]
    ) -> Dict[str, Any]:
        """
        Get check-in month data
        
        Args:
            start_time: Start time
            end_time: End time
            user_ids: List of user IDs
            
        Returns:
            Month data
        """
        return self.client.post_json("checkin/getcheckinmonthdata", json_data={
            "starttime": start_time.strftime("%Y-%m-%d %H:%M:%S"),
            "endtime": end_time.strftime("%Y-%m-%d %H:%M:%S"),
            "useridlist": user_ids
        })
    
    def get_checkin_schedulist(
        self,
        start_time: datetime,
        end_time: datetime,
        user_ids: List[str]
    ) -> Dict[str, Any]:
        """
        Get check-in schedule list
        
        Args:
            start_time: Start time
            end_time: End time
            user_ids: List of user IDs
            
        Returns:
            Schedule list
        """
        return self.client.post_json("checkin/getcheckinschedulist", json_data={
            "starttime": start_time.strftime("%Y-%m-%d %H:%M:%S"),
            "endtime": end_time.strftime("%Y-%m-%d %H:%M:%S"),
            "useridlist": user_ids
        })
    
    def get_checkin_day_data(
        self,
        start_time: datetime,
        end_time: datetime,
        user_ids: List[str]
    ) -> Dict[str, Any]:
        """
        Get check-in day data
        
        Args:
            start_time: Start time
            end_time: End time
            user_ids: List of user IDs
            
        Returns:
            Day data
        """
        return self.client.post_json("checkin/getcheckindaydata", json_data={
            "starttime": start_time.strftime("%Y-%m-%d %H:%M:%S"),
            "endtime": end_time.strftime("%Y-%m-%d %H:%M:%S"),
            "useridlist": user_ids
        }) 