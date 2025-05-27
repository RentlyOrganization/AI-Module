package com.example.AI.Controllers;

import com.example.AI.Payloads.Requests.PriceCityRequest;
import com.example.AI.Payloads.Requests.PriceEstimateRequest;
import com.example.AI.Payloads.Requests.PriceRateRequest;
import com.example.AI.Payloads.Requests.PriceTrendRequest;
import com.example.AI.Payloads.Responses.GroqResponse;
import com.example.AI.Services.GroqService;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/ai")
public class GroqController {

    private final GroqService groqService;

    public GroqController(GroqService groqService) {
        this.groqService = groqService;
    }

    @PostMapping("/rate_price")
    public ResponseEntity<GroqResponse> ask(@RequestBody PriceRateRequest priceRateRequest) {
        GroqResponse response = new GroqResponse(this.groqService.ratePrice(priceRateRequest));
        return ResponseEntity.ok(response);
    }

    @PostMapping("/estimate_price")
    public ResponseEntity<GroqResponse> estimate(@RequestBody PriceEstimateRequest priceEstimateRequest) {
        GroqResponse response = new GroqResponse(this.groqService.estimatePrice(priceEstimateRequest));
        return ResponseEntity.ok(response);
    }

    @PostMapping("/trend_price")
    public ResponseEntity<GroqResponse> trend(@RequestBody PriceTrendRequest priceTrendRequest) {
        GroqResponse response = new GroqResponse(this.groqService.getTrends(priceTrendRequest));
        return ResponseEntity.ok(response);
    }

    @PostMapping("/city_price")
    public ResponseEntity<GroqResponse> cityPrice(@RequestBody PriceCityRequest priceCityRequest) {
        GroqResponse response = new GroqResponse(this.groqService.cityInfo(priceCityRequest));
        return ResponseEntity.ok(response);
    }


}
